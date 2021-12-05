import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
# import wolframalpha
import json
import requests

import keyboard

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


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Jarvi is shutting down,Good bye')
            print('your personal assistant Jarvi is shutting down,Good bye')
            break
        if "enter" in statement or  "go on" in statement or "move on" in statement:
           keyboard.press_and_release('enter')
            
        elif "tab" in statement:
            keyboard.press_and_release('tab')
        elif "close" in statement:
            keyboard.press_and_release('F3')
        elif "open production" in statement:
            webbrowser.open_new_tab("https://ccamqa1e.utccgl.com:20105/grid/ui/#/M3BE_15.1_PRD")
            speak("Prod grid is open now")
        #else:
        #    keyboard.write(statement)

time.sleep(3)












