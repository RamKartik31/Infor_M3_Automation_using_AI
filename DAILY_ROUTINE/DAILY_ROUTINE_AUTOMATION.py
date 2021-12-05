import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import subprocess
import sys


print('Loading your AI personal assistant - Jarvi')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def readAvailableOptions():
    speak("Select an option from the below \n 1. CUSTOMER PAYER DIFFERENT\n 2. SPOT 8888 \n 3. CONTRACTS WITH NOT CODE \n 4. STUCK JOBS \n 5. STUCK JOBS GL037_47 \n 6. SPOT ASSETS TO BE ACTIVATED")
    print("Select an option from the below \n 1. CUSTOMER PAYER DIFFERENT\n 2. SPOT 8888 \n 3. CONTRACTS WITH NOT CODE \n 4. STUCK JOBS \n 5. STUCK JOBS GL037_47 \n 6. SPOT ASSETS TO BE ACTIVATED")

    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Jarvi")
wishMe()


while True:
    readAvailableOptions()
    speak("Tell me how can I help you now?")
    statement = takeCommand().lower()
    if statement==0:
        continue
        
    if "script" in statement:
        print("Running BOCA form script")
        subprocess.run([sys.executable,'test.py'])


    if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
        speak('your personal assistant Jarvi is shutting down,Good bye')
        print('your personal assistant Jarvi is shutting down,Good bye')
        break


time.sleep(3)












