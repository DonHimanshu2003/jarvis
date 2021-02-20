import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
from  requests import get

engine = pyttsx3.init('sapi5')
Voices = engine.getProperty('voices')
engine.setProperty('Voice',Voices[0].id)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")
    elif hour>12 and hour<18:
        Speak("Good Afternoon")
    elif hour>18 and hour<20:
        Speak("Good Evening")
    else:
        Speak("Good Night")

    Speak("I am Ashok Panda .Please tell me how may i help you")

def takecommand():
    R=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        R.pause_threshold = 1
        audio = R.listen(source)
    try:
        print("Recognizing ...")
        query=R.recognize_google(audio,language='en-in')
        print("User said:",query)

    except Exception as e :
        print(e)
        print("Say that again ... ")  
        return "None"
    return query

wishMe()

#while True:
query = takecommand().lower()
#Logic for executing tasks based on query

if 'ip address' in query:
    ip = get('https://api.ipify.org').text
    Speak("Your IP address is:: {}".format(ip))

elif 'wikipedia' in query:
    Speak('Searching wikipedia ...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=4)
    Speak("According to wikipedia")
    print(results)
    Speak(results)

elif 'open youtube' in query:
    webbrowser.open("www.youtube.com")

elif 'open google' in query:
    Speak("what do u want from google")
    cm = takecommand().lower()
    webbrowser.open(f"{cm}")

elif 'open facebook' in query:
    webbrowser.open("www.facebook.com")    

elif 'open instagram' in query:
    webbrowser.open("www.instagram.com")

elif 'send message' in query:
    pywhatkit.sendwhatmsg_to_group("+918010088779","Kaise ho",12,30)

elif 'Songs on youtube' in query:
    pywhatkit.playonyt("Raat Di Gedi")

elif 'open stackoverflow' in query:
    webbrowser.open("www.stackoverflow.com")

elif 'the time' in query:
    strTime=datetime.datetime.now().strTime("%H:%M::%S")
    Speak("Hey buddy, the time is {}".format(strTime))

elif 'open notepad' in query:
    apath = "C:\\Windows\\system32\\notepad.exe"
    os.startfile(apath)

elif 'open command prompt' in query:
    os.system("start cmd")

elif 'open adobe reader' in query:
    fpath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
    os.system("fpath")


 
