#!/usr/bin/python
#coding=utf-8
"""
Unicode Split Up 2010 by Sven-S. Porst / earthlingsoft
ssp-web@earthlingsoft.net
Enjoy the service at http://earthlingsoft.net/unicode/split-up
Or use the UnicodeChecker Mac application for more Unicode tools: http://earthlingsoft.net/UnicodeChecker/
"""



import cgi
import re
import unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



"""
	UTILITY FUNCTIONS *****************************************************************
"""

ampRegexp = re.compile(r"&")
ltRegexp = re.compile(r"<")
gtRegexp = re.compile(r">")
aposRegexp = re.compile(r"'")


def escapeHTML(inputString):
	"""
		Input: string
		Output: input string with < > & ' replaced by their HTML character entities
	"""
	escapedString = ampRegexp.sub('&amp;', inputString)
	escapedString = ltRegexp.sub('&lt;', escapedString)
	escapedString = gtRegexp.sub('&gt;', escapedString)
	escapedString = aposRegexp.sub('&#39;', escapedString)

	return escapedString





"""
	FUNCTIONS *****************************************************************
"""


def headMarkup ():
	headMarkup = ["""Content-type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
<head>
	<title>Split up Unicode Strings</title>
	<style type="text/css">
		body {
			background: #f9e8d0;
			font-family: "Palatino", Georgia, serif;
			margin: auto;
			max-width: 60em;
			color: #111;
		}
		h1 {
			font-size: 144%;
			margin: 1em;
			font-style: italic;
			text-align: center;
		}
		form {
			text-align: center;
		}
		form input {
			font-size: 120%;
		}
		form input.text {
			width:70%;
		} 
		table {
			margin: 1em auto;
			border-spacing: 0px;
		}
		table .no {
			text-align: right;
			color: #c6b6a4;
		}
		table .char {
			font-size: 144%;
			text-align: center;
		}
		table .hex, table .dec {
			text-align: right;
			font-family: Menlo, "Andale Mono", fixed;
			color: #666;
		}
		.hex0x {
			color: #c6b6a4;
		}
		table .name {
			text-align: left;
			text-transform: lowercase;
			color: #666;
		}
		tr.combining {
			background: #f5d3d5;
		}
		
		tr.control {
			background: #f5d3d5;
		}
		tr.control td.name:after, tr.combining td.name:after {
			content: "– Control Character";
			font-style: italic;
			text-transform: none;
			color: #111;
		}
		tr.combining td.name:after {
			content: "– Combining Character";
		}
		th {
			font-family: "Palatino", Georgia, serif !important;
			font-style: italic;
			font-size: 100% !important;
			font-weight: normal !important;
			text-transform: none !important;
			padding: 0.5em;
		}
		td {
			padding: 0em 0.5em;
		}
	</style>
</head>"""]

	qS = "" 
	if form.has_key("q"):
		qS = unicode(form["q"].value)

	headMarkup += ["""<body>
	<h1>Split Up Unicode Strings</h1>
	<form>
		<input name="q" placeholder="Your String Here" autofocus class="text" value='""", escapeHTML(qS), """'>
		<input type="submit" value="Split Up">
	</form>
"""]
	return headMarkup




def footMarkup():
	footMarkup = ["</body>\n</html>"]
	return footMarkup



def tableHeadMarkup():
	tableHeadMarkup = ["""\n	<table>\n			<tr><th class='no'>#</th><th class='char'>Char</th><th class='hex'>Hex</th><th class='dec'>Dec</th><th class='name'>Name</th>\n"""]
	return tableHeadMarkup


def tableFootMarkup():
	tableFootMarkup = ["	</table>"]
	return tableFootMarkup


def hexMarkup(char):
	hexString = hex(ord(char))[2:]
	zeroFiller = (4-len(hexString)) * "0"
	hexMarkup = """<span class="hex0x">U+""" + zeroFiller + "</span>" +  hexString
	
	return hexMarkup
	


def tableRowMarkupForCharacterAtPosition(char, position):
	rowstyle = []
	if unicodedata.combining(char) <> 0:
		rowstyle += ["combining"]
	if ord(char) < 127:
		rowstyle += ["ASCII"]
	if unicodedata.category(char) == "Cc":
		rowstyle += ["control"]
	normalisation = unicodedata.normalize("NFD", char)

	rowstylestring = ""
	if len(rowstyle) > 0:
		rowstylestring = " class='" + " ".join(rowstyle) + "'"

	markup = ["			<tr", rowstylestring, ">\n"]
	markup += ["				<td class='no'>", str(position),"</td>\n"]
	markup += ["				<td class='char'>", escapeHTML(char), "</td>\n"]
	markup += ["				<td class='hex'>", hexMarkup(char), "</td>\n"]
	markup += ["				<td class='dec'>", str(ord(char)), "</td>\n"]
	markup += ["				<td class='name'>", escapeHTML(unicodedata.name(char, "NAME UNKNOWN")), "</td>\n"]
	markup += ["		</tr>\n"]
	
	return markup



"""
	MAIN SCRIPT *****************************************************************
"""


form = cgi.FieldStorage()
output = headMarkup()
resultString = "";
if form.has_key("q"):
	queryString = unicode(form["q"].value)
	if len(queryString) > 0:
		output += tableHeadMarkup()
		position = 0
		for char in queryString:
			output += tableRowMarkupForCharacterAtPosition(char, position)
			position = position + 1
		output += tableFootMarkup()
output += footMarkup()
print "".join(output)