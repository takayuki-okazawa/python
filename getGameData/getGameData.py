#!/usr/bin/env python3

import re
from urllib import request

#Print Object
dayObjList1 = [];
dayObjList2 = [];
soccerList = [];
baseballList = [];

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
			timeArray = str2.split(".")
			#print("\n"+timeArray[1]+"月"+timeArray[2].split("（")[0]+"日")
			dayObjList1.append("\n"+timeArray[1]+"月"+timeArray[2].split("（")[0]+"日")

	#Time
	for str3 in re.findall('<td class="kickoff">(.*?)</td>',str1,re.S):

		if time[0]==str3:
			time[1] = time[1]+1
		elif ""!=time[0]:
			#print(time[0]+"    Jリーグ:"+str(time[1])+"試合")
			soccerList.append(dayObjList1[-1]+"$$"+time[0]+"    Jリーグ:"+str(time[1])+"試合")
			time[1] = 1
		time[0] = str3
		



### Baseball ###
url2 = "http://baseball.yahoo.co.jp/npb/schedule/"

src2 = request.urlopen(url2).read()
src2 = src2.decode('utf-8')

day2 = ''
time2 = ["",1]
daylist = ["a"]

for str1_2 in re.findall('<tr>(.*?)</tr>',src2,re.S):

	#Day
	for str2_2 in re.findall('" width="100"(.*?)</span></strong></th>',str1_2,re.S):
		
		str2_2 = re.sub('<br /><span class=(.*)>', '', str2_2)
		str2_2 = str2_2.split('<strong>')[1]

		if str2_2!=day2:
			day2 = str2_2

	#Time
	for str3_3 in re.findall('<em>(.*?)</em>',str1_2,re.S):

		_str3_3 = str3_3.split(' ')[0]

		if time2[0]==day2+_str3_3 and 1<len(str3_3.split(' ')):
			time2[1] = time2[1]+1

		elif 1<len(str3_3.split(' ')):

			if 1<len(time2[0].split("（")):

				if daylist[len(daylist)-1]!=time2[0].split("（")[0]:
					#print("\n"+time2[0].split("（")[0])
					dayObjList2.append("\n"+time2[0].split("（")[0])
					daylist.append(time2[0].split("（")[0]);

				#print(time2[0].split("）")[1]+"    プロ野球:"+str(time2[1])+"試合")
				baseballList.append(dayObjList2[-1]+"$$"+time2[0].split("）")[1]+"    プロ野球:"+str(time2[1])+"試合")
				time2[1] = 1

		time2[0] = day2+_str3_3
#Last Item		
#print(time2[0].split("）")[1]+"    プロ野球:"+str(time2[1])+"試合")
baseballList.append(dayObjList2[-1]+"$$"+time2[0].split("）")[1]+"    プロ野球:"+str(time2[1])+"試合")

#print
for dayObj in dayObjList1:
	print(dayObj)

	for soccerObj in soccerList:
		count = 0;

		if -1!=soccerObj.find(dayObj):
			print(soccerObj.split("$$")[1])

		baseballCount = 0

		for baseballObj in baseballList:
			if -1!=baseballObj.find(dayObj):
				++baseballCount

		if count <= baseballCount:
			print(baseballList[count].split("$$")[1])

		++count

