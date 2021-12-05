import pyautogui
import speech_recognition as sr
import pyttsx3
import keyboard
import time
import webbrowser
import pytesseract
import numpy as np
import cv2
import os
import image_diff_V2 

print('Press Ctrl-C to quit.')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
'''
positionStr = ''
while 1:
    # Get and print the mouse coordinates.
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
'''

# im_path = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_FullScreens\FAS001_B.jpg'
print('Got to M3 screen')
speak('Got to M3 screen')
time.sleep(3)
im = pyautogui.screenshot()
next_button_int_tuple =  pyautogui.locateOnScreen('next.jpg', confidence=0.9)
# next_button_int_tuple =  pyautogui.locateOnScreen('close.jpg', confidence=0.9)

print('next_button_int_tuple: '+str(next_button_int_tuple))
next_button_int_coordinates = pyautogui.center(next_button_int_tuple)
print('next_button_int_coordinates: '+str(next_button_int_coordinates))
pyautogui.click(next_button_int_coordinates)