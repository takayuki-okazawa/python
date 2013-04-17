#!/usr/bin/env python3

import re
from urllib import request

# Succer
url1 = "http://www.j-league.or.jp/schedule/"
#,"http://baseball.yahoo.co.jp/npb/schedule/"


src = request.urlopen(url1).read()
src = src.decode('shift-jis')

day = ''
time = ["",1]

#here editing
for str1 in re.findall('(<tr class="odd">|<tr class="even">).*</tr>',src,re.S):
	print(str1)
	#Day
	for str2 in re.findall('<td class="day">(.*?)</td>',str1,re.S):
		
		if str2!=day:
			day = str2
			#print("\n\n"+str2)

	#Time
	for str3 in re.findall('<td class="kickoff">(.*?)</td>',str1,re.S):

		if time[0]==str3:
			time[1] = time[1]+1
		elif ""!=time[0]:
			#print(time[0]+"    Jリーグ:"+str(time[1])+"試合")
			time[1] = 1
		time[0] = str3
		





#<tr class="odd">
#<tr class="even">