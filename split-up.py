#!/usr/bin/python
#coding=utf-8

import cgi
import re
import unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")




"""
	MAIN SCRIPT *****************************************************************
"""

print """Content-type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
<head>
	<title>Split up Unicode Strings</title>
	<style type="text/css">
		body { background: #f9e8d0; font-family: "Hoefler Text", Georgia, serif; margin:auto; max-width: 50em;}
		table .no { text-align:right; color: #666; }
		table .char { font-size:144%; text-align:center; }
		table .hex { text-align:right; }
		table .name { text-align:left; text-transform:lowercase; }
		th { font-size: 100%!important; text-transform:uppercase!important; margin: 0px 0.8em;}
		td { }
	</style>
</head>
<body>
	<h1>Split Up Unicode Strings</h1>
	<p>
	<form>
		<input name="q" placeholder="Your String Here" autofocus>
		<input type="submit" value="Split Up">
	</form>
	</p>
"""

form = cgi.FieldStorage()
resultString = "";
if form.has_key("q"):
	queryString = unicode(form["q"].value)
	if len(queryString) > 0:
		print """
			<table>
			<tr><th class='no'>#</th><th class='char'>Char</th><th class='hex'>Hex</th><th class='name'>Name</th>"""
		index = 0
		for char in queryString:
			rowstyle = []
			if unicodedata.combining(char) <> 0:
				rowstyle += ["combining"]
			rowstylestring = ""
			if len(rowstyle) > 0:
				rowstylestring = " class='" + " ".join(rowstyle) + "'"
			print "				<tr" + rowstylestring + "><td class='no'>" + str(index) + "</td><td class='char'>" + char + "</td><td class='hex'>" + hex(ord(char)) + "</td><td class='name'>" + unicodedata.name(char) + "</td></tr>"
			index = index + 1
			
		print "			</table>"
			
print """
</body>
</html>
"""