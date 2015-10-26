#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  freevpn_reader.py 
#  
#  Kyle Kerr birdmunone@yahoo.com
#  10-25-2015
#  This program looks for the password for vpnbook's freevpn service and stores
#  it in the clipboard.
#  pyperclip and, for linux, xclip are required to allow it to function. It
#  hasn't been tested on anything but bodhi linux, a distro based on ubuntu.

import urllib, pyperclip

filehandle = urllib.urlopen('http://www.vpnbook.com/freevpn')
flag = 0

for lines in filehandle.readlines():
	if (lines.find('Password') is not -1 and flag == 0):
		print('The current password for freevpn is:')
		print lines[lines.find('strong') + 7:lines.find('</')]
		pyperclip.copy(lines[lines.find('strong') + 7:lines.find('</')])
		flag = 1

filehandle.close()
