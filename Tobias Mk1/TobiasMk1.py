# comment
import pyttsx3 #pip install pyttsx3
import datetime #gets date and time
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import requests #pip install requests
import smtplib #pip intall smtplib
import psutil #pip install psutil
import webbrowser #pip install webbrowser
import bs4 #pip install webbrowser
import sys #pip install sys
engine = pyttsx3.init()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time_():
	Time=datetime.datetime.now().strftime("%I:%M") #12 hour clock
	speak("The current time is")
	speak(Time)

def date_():
	Date=datetime.datetime.now().strftime("%B:%d, %Y") #month day year
	speak("The date is" + Date)

def battery_():
	battery= psutil.sensors_battery()
	speak('the battery is at' + str(battery.percent) + 'percent')

def version_():
	v= "0.9"
	speak("This is Tobias Mark 1 version" + v)

def name_():
	speak("My name is Tobias. That stands for 'Tavion's original but intelligent artificial system'")

def creator_():
	speak("I was created by Tavion Britt. Tobias Mark 1 began production on May 14, 2021")

def bday_():
	speak("My birthday is May 14, 2021")

def age_():
	bmonth = 5
	byear = 2021
	bday = 14
	year = int(datetime.datetime.now().strftime("%Y"))
	month = int(datetime.datetime.now().strftime("%m"))
	day = int(datetime.datetime.now().strftime("%d"))
	yrs = year - byear
	months = month - bmonth
	if months<0:
		months = months+12

	if yrs<1 and months<1:
		age = day - bday
		age = str(age)
		speak("I am" + age + "days old")

	elif yrs<1:
		#convert back to string
		months = str(months)
		speak("I am" + months + "months old")

	else:
		#convert back to string
		months = str(months)
		yrs = str(yrs)
		speak("I am" + yrs + "years and" + months + "months old")

def quit_():
	speak("turning off")
	exit()

def weather_():
	x = query.split('in')
	place = x[1]
	url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=da1b3912cd52cc458f77d90cae5c2986".format(place)
	res=requests.get(url)
	data=res.json()
	temp=data['main']['temp']
	temp = str(temp)
	speak("The temperature in " + place + " is " + temp)

def localWeather_():
	url="http://api.openweathermap.org/data/2.5/weather?q=Fredericksburg&units=imperial&appid=da1b3912cd52cc458f77d90cae5c2986"
	res=requests.get(url)
	data=res.json()
	temp=data['main']['temp']
	speak("The weather in Fredericksburg is")
	speak(str(temp))
	
def news_():
	speak("what news do you want to hear about?")
	idea= takeCommand().lower()
	url="https://newsapi.org/v2/everything?q={}&apiKey=c94c3e70068b4dd2b53c2586b45a905d".format(idea)
	res=requests.get(url)
	data=res.json()
	articles=data['articles']
	results=[]
	for art in articles:
		results.append(art['title'])
	for i in range(0,1):
		news=results[i]
		speak(news)

def topNews_():
	url="https://newsapi.org/v2/top-headlines?country=us&apiKey=c94c3e70068b4dd2b53c2586b45a905d"
	res=requests.get(url)
	data=res.json()
	articles=data['articles']
	results=[]
	for art in articles:
		results.append(art['title'])
	speak("your top news")
	for i in range(0,3):
		item=results[i]
		news=item.split("-")
		speak(str(i+1))
		speak(news[0])
		speak("published by " + news[1])

def math_():
	numbers = []
	for x in query: #loop through to get number
		if x.isdigit():
			num1 = x
			num1 = int(num1)
			numbers.append (num1)
	num1 = numbers[0]
	num2 = numbers[1]
	if "+" in query:
		ans = num1 + num2
		speak(str(num1) + " plus " + str(num2) + " equals " + str(ans))
	
	elif "-" in query:
		ans = num1 - num2
		speak(str(num1) + " minus " + str(num2) + " equals " + str(ans))


def setAlarm_():
	for x in query: #gets hour of alarm
		if x.isdigit():
			hour = x
	hour = int(hour) #makes it a int

	if "a.m." in query or "morning" in query:
		speak("adding" + str(hour) + "a m alarm")
		alarms.append(hour)
	elif "p.m." in query or "afternoon" in query or "night" in query:
		newHour = hour + 12
		speak("adding" + str(hour) + "p m alarm")
		alarms.append(newHour)
	

def deleteAlarm_():
	counter = 0
	for x in alarms:
		if x > 12:
			res = x -12
			speak('do you want to delete your' + str(res) + "p m alarm?")
			ip = takeCommand().lower()
			if ip == 'yes':
				alarms.pop(counter)
			counter += 1
		else:
			speak('do you want to delete your' + str(x) + "a m alarm?")
			ip = takeCommand().lower()
			if ip == 'yes':
				alarms.pop(counter)
			counter += 1

def viewAlarms_():
	speak("you have " + str(len(alarms)) + "alarms")
	for x in alarms:
		if x > 12:
			res = x -12
			speak(str(res) + "p m")
		else:
			speak(str(x) + "a m")

def wishme():
	#greeting
	hour = datetime.datetime.now().hour
	if hour<12:
		speak('Good morning Mr. Britt')
	elif hour>12 and hour<22:
		speak('Good afternoon Mr. Britt')
	time_()
	date_()

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening.....")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try:
		print("recogninzing.........")
		query = r.recognize_google(audio,language='en-US')
		print(query)

	except Exception as e:
		print(e)
		print("say that again please...")
		speak("say that again please")
		return "None"
	return query


if __name__ == '__main__':
	wishme()
	alarms = []
	while True:
		query = takeCommand().lower()

		#All commands will be stored in lower case in query for easy recognition
		if 'tobias' in query and 'time' in query:
			time_()

		if 'tobias' in query and 'date' in query:
			date_()

		if 'tobias' in query and 'version' in query:
			version_()

		if 'tobias' in query and 'name' in query:
			name_()

		if 'tobias' in query and 'birthday' in query:
			bday_()

		if 'tobias' in query and 'inventor' in query or 'creator' in query:
			creator_()

		if 'tobias' in query and 'age' in query or 'old' in query:
			age_()

		if 'tobias' in query and 'wikipedia' in query:
			query=query.replace('wikipedia', '')
			try:
				result=wikipedia.summary(query,sentences=3)
				speak("according to wikipedia " + result)
			except Exception as e:
				print(e)
				speak("could not find page")

		if 'tobias' in query and 'in' in query and 'weather' in query:
			weather_()

		elif 'tobias' in query and 'weather' in query or 'temperature' in query:
			localWeather_()

		if 'tobias' in query and 'top news' in query or 'news report' in query:
			topNews_()

		elif 'tobias' in query and 'news' in query:
			news_()

		if 'tobias' in query and 'battery' in query:
			battery_()

		if 'tobias' in query and 'set' in query and 'alarm' in query:
			setAlarm_()

		if 'tobias' in query and 'delete' in query and 'alarm' in query:
			deleteAlarm_()

		if 'tobias' in query and 'my alarms' in query and 'view alarms' in query:
			viewAlarms_()

		if 'tobias' in query and 'minus' in query or 'plus' in query or '+' in query or '-' in query:
			math_()

		if 'tobias' in query and 'turn off' in query or 'power off' in query or 'exit' in query or 'quit' in query:
			quit_()