import pyttsx3 as pyt
import datetime as dt
import pywhatkit
import speech_recognition as sp
import webbrowser as web
import os
import pyjokes
import smtplib
import wikipedia as googleScrap
import requests
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
from bs4 import BeautifulSoup
engine= pyt.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)

    engine.runAndWait()
def wishme():
    hours=int(dt.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("Good Morning Sir!")
        print("Good Morning Sir!")
    elif hours>=12 and hours<18:
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")
    speak("Namaste Sir ji")
    print("Namaste Sir ji")
def takecommands():
    '''It will take y
    our voice through mic as a command for doing work'''
    r=sp.Recognizer()
    with sp.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='eng-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Please say that again")
        return "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ayush4091@gmail.com','gvuqqqlsfinxrldn')
    server.sendmail('ayush4091@gmail.com',to,content)
    server.close()
def search():
    print("what do you want to search ?")
    speak("what do you want to search ?")
    q1 = takecommands()
    pywhatkit.search(q1)
    result=googleScrap.summary(q1,3)
    print(result)
    speak(result)
def My_location():
    ip_add=requests.get('https://api.ipify.org').text
    url='https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
    geo=requests.get(url)
    geo1=geo.json()
    state=geo1['city']
    country=geo1['country']
    print(f"sir ji you are now in {state} {country}")
    speak(f"sir ji you are now in {state} {country}")
def googlemaps(place):
    url_place="https://www.google.com/maps/place/"+str(place)
    geolocator=Nominatim(user_agent="myGeocoder")
    location=geolocator.geocode(place,addressdetails=True)
    target_latlon=location.latitude,location.longitude
    location=location.raw['address']
    target={'city':location.get('city',''),
            'state':location.get('state',''),
            'country':location.get('country','')}
    current_loca=geocoder.ip('me')
    current_latlon=current_loca.latlng
    distance=str(great_circle(current_latlon,target_latlon))
    distance=str(distance.split(' ',1)[0])
    distance=round(float(distance),2)
    print(f"target location is {target}")
    speak(f"target location is {target}")
    print(f"Sir ji distance is {distance}")
    speak(f"Sir ji distance is {distance}")
def temp():
    print("Tell me the place-")
    speak("Tell me the place-")
    place=takecommands()
    url="https://www.google.com/search?q="+"temprature in"+str(place)
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temperature=data.find("div",class_="BNeawe").text
    print(f"Temperature is {temperature} celcius")
    speak(f"Temperature is {temperature} celcius")
def setname():
    print("what name you want to give me ?")
    speak("what name you want to give me ?")
    try:
        name=takecommands().lower()
        print(f"From now i am{name}")
        speak(f"From now i am {name}")
        return name
    except:
        print("say that again")
        speak("say that again")
if __name__ == '__main__':
    wishme()
    name=setname()
    while True:
       query=takecommands().lower()
       if name in query:
           # logic to implement tasks
           query=query.replace(name,"")
           if 'search' in query:
               try:
                   search()
               except:
                   print("Can you repeat sir ?")
                   speak("Can you repeat sir ?")
                   q=takecommands()
                   if q == "sure":
                       search()
           if "you can go" in query:
               speak("ok sir ji mein chalta hu")
               print("ok sir ji mein chalta hu")
               break
           elif "how are you" in query:
               speak("I am fine sir ji")
               print("I am fine sir ji")
           elif 'open youtube' in query:
               web.open("youtube.com")
               speak("opened sir ji")
           elif 'open google' in query:
               web.open("google.com")
               speak("Openend sir ji")
           elif 'open gmail' in query:
               web.open('gmail.com')
               speak("Openend sir ji")
           elif "let's do some designing" in query:
               os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Illustrator 2021")
               speak("Openend sir ji")
           elif "opera" in query:
               os.startfile(
                   r"C:\Users\Ayush Sharma\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Opera GX Browser")
               speak("Openend sir ji")
           elif "play family guy" in query:
               web.open('https://www.youtube.com/watch?v=D4QnQBkdgrU')
               speak("Openend sir ji")
           elif "let's code" in query:
               path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3\\bin\\pycharm64.exe"
               os.startfile(path)
               speak("Openend sir ji")
           elif "canva" in query:
               web.open("canva.com")
           elif "joke" in query:
               myjoke = pyjokes.get_joke(language='en', category='all')
               speak(myjoke)
               print(myjoke)
           elif "the time" in query:
               time = dt.datetime.now().strftime("%H:%M:%S")
               print(time)
               speak(time)
           elif "send email" in query:
               try:
                   speak("ok sir ji")
                   to = '1900300100055@ipec.org.in'
                   speak("What should i say?")
                   content = takecommands()
                   sendemail(to, content)
                   speak("sent it sir ji")
               except Exception as e:
                   print(e)
                   speak("Sorry sir ji i couldn't make it")
           elif "play song" in query:
               try:
                   print("which song you want to listen ?")
                   speak("which song you want to listen ?")
                   song=takecommands().lower()
                   try:
                       speak("ok sir ji playing"+song)
                       pywhatkit.playonyt(song)
                   except:
                       speak("Can you repeat ?")
               except:
                   speak("Can you repeat ?")
           elif "click my pic" in query:
               try:
                   print("sure sir ji,Smile Please!")
                   speak("sure sir ji,Smile Please!")
                   cam=VideoCapture(0)
                   s,img = cam.read()
                   if s:
                       imshow("cam-test",image)
                       imwrite("Geeksforgeeks.png",image)
                       waitkey(0)
                       destroywindow("GeeksforGeeks")
               except:
                   print("Sorry I couldn't sir ji!")
                   speak("Sorry I couldn't sir ji!")
           elif 'my location' in query:
               try:
                   My_location()
               except:
                   print("Can you please say that again ?")
                   speak("Can you please say that again ?")
           elif 'locate' in query:
               try:
                   print("okk sir tell me target location")
                   speak("okk sir tell me target location")
                   target=takecommands()
                   googlemaps(target)
               except:
                   print("Sorry I couldn't sir ji!")
                   speak("Sorry I couldn't sir ji!")
           elif "temperature" in query:
               try:
                   temp()
               except:
                   print("Sorry I couldn't sir ji!")
                   speak("Sorry I couldn't sir ji!")