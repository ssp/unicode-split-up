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
	<meta name="description" content="Splits up a string into its Unicode codepoints. Reveals names, Unicode hex and combining characters in the process.">
	<meta name="keywords" content="unicode split string text">
	<meta name="viewport" content="width=400">
	<link rel="author" href="mailto:(Sven-S.%20Porst)%20ssp-web@earthlingsoft.net">
	<link rel="shortcut icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXRFWHRDb21tZW50ACCyRK3OAAACh0lEQVR4nGRTvU/aYRB+EALSJqVNGGSALupQTCCCEZDBKCGIHwE7khQWNOFfsVt3CUMXBw1GHUyMDhr+gYahMQTj4Ec6MPAVLPx6zxVIPy65/O5975675+69H/C3uC0WS8RmsyWtVmta9ONQU7wTX1Ri3uNfMZlMfq/X+y2VShnZbNbY2dkxdnd3jUKhoEqbd7lczkin08b09HSFxYidIF7AXzc2Nrzb29uQBJBA5PN5JJNJrK2tqc07+tbX17G5uRnyeDxfRgk8kvGDJEE0GoXb7cbU1BR6vR5ubm5wfX2Nbrerd/QtLy9jZmYGgokJ1mwym82hTCZTYQUGSDt4enrCycmJ2tSXlxdWhcvl0par1SqKxSKOjo5cE5LgjQwIMiiIjefnZ5TLZfj9/nE7q6urODs7w+PjI2SQsNvtmJycZPJ3bMHKKkxAMAPb7TZqtRr29/dRKpWwsLAAFiErJqFNjIjNwjmIoNVq4erqCo1GQ6s8PDwodZ/Pp3f0dzodLRAKhUYJTGRgiCglDocOngeDAebm5vQlDg4OFEwfY9gCY/QV5PLn6BAOh5UuwRQyOT09xd3dnYIDgQAikcifK9S3CLjV7/eVLhORHr+VSgUOh4P96Xl+fl7BtBk/LNqbEOCPZrOpFPG7nzETVq7X6wgGg1haWlIfmTCWBUWanIQ9Fos1ZAutfC7SHq43Li8vFbSysjLumQt2fn6O4+PjzsXFxVsdpWxZSXb80+zsrC4Th8REo0XiTFiRz3t/f4/b21scHh6WZOFyo2G8djqde4uLi7VEItGVrTOoW1tbqqNzPB7vSMx3if0smFfK9L9fU/Z76LQNbcb0Rbui7aE9ll8AAAD//wMAOQswwpMoWiMAAAAASUVORK5CYII=">
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
		#main {
			width: 70%;
			margin: auto;
		}
		p {
			margin: 1em auto;
			text-align: center;
		}
		form {
			text-align: center;
			margin-bottom: 2em;
		}
		form input {
			font-size: 120%;
		}
		form input.text {
			width:60%;
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
		table .dec {
			display: none;
		}
		table .hex, table .dec {
			text-align: right;
			font-family: Menlo, "Andale Mono", fixed;
			color: #666;
		}
		.hex0x {
			color: #d2c1ae;
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
			color: #111 !important;
		}
		td {
			padding: 0em 0.5em;
		}
		#foot {
			margin: 1em;
			padding-top: 2em;
			width: 80%;
			font-style: italic;
			margin: auto;
			text-align: center;
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
	footMarkup = ["""	</div>
	<div id="foot">
	<hr>
	<p>	
		A service by <a href="http://earthlingsoft.net">earthlingsoft</a> 
		·
		<a href="mailto:ssp-web@earthlingsoft.net?subject=Unicode%20Split%20Up">Send Feedback</a>
	</p>
	<p>
		Finding this tool useful and using a Mac? Then try our <a href="http://earthlingsoft.net/UnicodeChecker/">UnicodeChecker</a> application!
	</p>
	</div>
</body>\n</html>"""]
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
else:
	output += ["""	<p>
		Enter the string you want to split up and click the »Split Up« button.
	</p><p>
		The site will then display information on each codepoint in the string and highlight combining characters.
	</p>
"""]
output += footMarkup()
print "".join(output)