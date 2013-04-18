#!/usr/bin/env python3

import re
from urllib import request

### Soccer ###

url1 = "http://www.j-league.or.jp/schedule/"

src = request.urlopen(url1).read()
src = src.decode('shift-jis')

day = ''
time = ["",1]

for str1 in re.findall('<tr class="(.*?)</tr>',src,re.S):
	
	#Day
	for str2 in re.findall('<td class="day">(.*?)</td>',str1,re.S):
		
		if str2!=day:
			day = str2
			print("\n"+str2)

	#Time
	for str3 in re.findall('<td class="kickoff">(.*?)</td>',str1,re.S):

		if time[0]==str3:
			time[1] = time[1]+1
		elif ""!=time[0]:
			print(time[0]+"    Jリーグ:"+str(time[1])+"試合")
			time[1] = 1
		time[0] = str3
		



### Baseball ###
url2 = "http://baseball.yahoo.co.jp/npb/schedule/"

src2 = request.urlopen(url2).read()
src2 = src2.decode('utf-8')

day2 = ''
time2 = ["",1]

for str1_2 in re.findall('<tr>(.*?)</tr>',src2,re.S):
	
	#print("*** = "+str1_2)

	#Day
	for str2_2 in re.findall('ct" width="100"(.*?)</span></strong></th>',str1_2,re.S):
		
		str2_2 = re.sub('<br /><span class=(.*)>', '', str2_2)
		str2_2 = str2_2.split('<strong>')[1]

		if str2_2!=day2:
			day2 = str2_2
			#time2 = ["",1]
			print("\n"+str2_2)

	#Time
	for str3_3 in re.findall('<em>(.*?)</em>',str1_2,re.S):

		if ''!=str3_3.split(' '):

			str3_3 = str3_3.split(' ')[0]

			if time2[0]==str3_3:
				time2[1] = time2[1]+1
			#elif ""!=time2[0]:
			print(day2+time2[0]+"    プロ野球:"+str(time2[1])+"試合")
			time2[1] = 1
			time2[0] = str3_3
