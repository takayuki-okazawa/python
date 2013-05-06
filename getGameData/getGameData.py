#!/usr/bin/env python3

import re
from urllib import request
from datetime import datetime, date, time

dayList = []
printArray = []
year = date.today().year



### Soccer ###
url1 = "http://www.j-league.or.jp/schedule/"

src = request.urlopen(url1).read()
src = src.decode('shift-jis')
day = ''
initFlag = False

for str1 in re.findall('<tr class="(.*?)</tr>',src,re.S):
	
	#Day
	for str2 in re.findall('<td class="day">(.*?)</td>',str1,re.S):
		if str2!=day:
			day = str2
			timeArray = str2.split(".")
			dayList.append(timeArray[1]+"月"+timeArray[2].split("（")[0]+"日")

	#Time
	for str3 in re.findall('<td class="kickoff">(.*?)</td>',str1,re.S):

		if 0<len(printArray):
			beforeTime = printArray[-1]["time"]
		else:
			beforeTime = "hoge"

		if beforeTime==str3:
			printArray[-1] = {"date":dayList[-1], "time":str3, "soccer":(printArray[-1]["soccer"]+1), "baseball":""}
		else:
			printArray.append({"date":dayList[-1], "time":str3, "soccer":1, "baseball":""})


### Baseball ###
url2 = "http://baseball.yahoo.co.jp/npb/schedule/"

src2 = request.urlopen(url2).read()
src2 = src2.decode('utf-8')

day2 = ''
time2 = ["",1]
baseballDayList = ["a"]
lastTime = ""

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
		lastTime = _str3_3

		if time2[0]==day2+_str3_3 and 1<len(str3_3.split(' ')):
			time2[1] = time2[1]+1

		elif 1<len(str3_3.split(' ')):

			if 1<len(time2[0].split("（")):

				if baseballDayList[len(baseballDayList)-1]!=time2[0].split("（")[0]:
					
					if (time2[0].split("（")[0]) not in dayList:
						dayList.append(time2[0].split("（")[0])

					baseballDayList.append(time2[0].split("（")[0])

				printArray.append({"date":dayList[-1], "time":_str3_3, "soccer":"", "baseball":str(time2[1])})
				time2[1] = 1

		time2[0] = day2+_str3_3

#Last Item		
printArray.append({"date":dayList[-1], "time":lastTime, "soccer":"", "baseball":str(time2[1])})


#sort
flag = True
while flag == True:
	flag = False

	for i in range(len(dayList)):
		_dayList1 = dayList[i].split("月")
		_dayList2 = _dayList1[1].split("日")

		object1 = date(year,int(_dayList1[0]),int(_dayList2[0]))

		if (i+1)<len(dayList):
			_dayList1 = dayList[i+1].split("月")
			_dayList2 = _dayList1[1].split("日")
			object2 = date(year,int(_dayList1[0]),int(_dayList2[0]))

			if object1>object2:
				flag = True
				obj1 = dayList[i]
				obj2 = dayList[i+1]
				dayList[i] = obj2
				dayList[i+1] = obj1


#print
for dayObj in dayList:
	print(dayObj)
	dayPrintObj = []
	dayTimeObj = []

	for printObj in printArray:
		if dayObj == printObj['date']:
			dayPrintObj.append(printObj)
			timeArray = printObj['time'].split(':')
			t = time(int(timeArray[0]),int(timeArray[1]))
			dayTimeObj.append(t)

	#sort
	flag = True
	while flag == True:
		flag = False

		for i in range(len(dayTimeObj)):

			if (i+1)<len(dayTimeObj) and dayTimeObj[i]>dayTimeObj[i+1]:
				flag = True
				object1 = dayTimeObj[i]
				object2 = dayTimeObj[i+1]
				dayTimeObj[i] = object2
				dayTimeObj[i+1] = object1

	#delete
	flag = True
	while flag == True:
		flag = False

		for i in range(len(dayTimeObj)):

			if (i+1)<len(dayTimeObj) and dayTimeObj[i]==dayTimeObj[i+1]:
				flag = True
				del dayTimeObj[i]


	for timeValue in dayTimeObj:
		soccerPrint = 0
		baseballPrint = 0

		for _dayPrintObj in dayPrintObj:
			timeArray = _dayPrintObj['time'].split(':')
			t = time(int(timeArray[0]),int(timeArray[1]))
			if timeValue == t:
				if ''!=_dayPrintObj["soccer"]:
					soccerPrint += int(_dayPrintObj["soccer"])
				if ''!=_dayPrintObj["baseball"]:
					baseballPrint += int(_dayPrintObj["baseball"])

		print(timeValue.strftime("%H:%M") + ' サッカー:'+str(soccerPrint)+' 野球:'+str(baseballPrint))






