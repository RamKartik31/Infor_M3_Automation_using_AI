# THIS IS A WORKING AUTOMATION CODE USING KEYBOARD ONLY
import speech_recognition as sr
import pyttsx3
import keyboard
import pyautogui
import time
import webbrowser
import pytesseract
import numpy as np
import cv2
import os
import image_diff_V2 

Assests = ['46063','46629','47000','47001','47175','47176','47226']

count = 0

FAS001_ProgramScreens_path = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\FAS001_ProgramScreens'
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def ExtractTemplate_fromFullScreen(small_image_p_in,large_image_p_in,count,threshold_ip,message): #better method than v2
     speak('Searching for panel '+message)
     # print(small_image_p_in)
     isPanelFound = 'No'    
     method = cv2.TM_CCOEFF_NORMED
     # Read the images from the file
     small_image = cv2.imread(small_image_p_in)
     large_image = cv2.imread(large_image_p_in)
     #cv2.imshow('SI',small_image)
     #cv2.namedWindow('output', cv2.WINDOW_NORMAL)  
     #cv2.imshow('output',large_image)
     #cv2.waitKey(0)

     w,h = small_image.shape[:2]
     
     res = cv2.matchTemplate(large_image,small_image,method)
     
     threshold = threshold_ip
     #print('res'+str(res))
     
     loc= np.where(res >= threshold)
     cropped_img_path = "NOT_FOUND"
     
     for pt in zip(*loc[::-1]):
        isPanelFound = 'Yes'
        cv2.rectangle(large_image,pt,(pt[0]+h,pt[1]+w),(0,0,255),2)
        if isPanelFound == 'Yes':
            cropped_img = large_image[pt[1]:pt[1]+w,pt[0]:pt[0]+h]
            cropped_img_path = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\FAS001_CroppedImages\\cropped_img_'+str(count)+'.jpg'
            cv2.imwrite(cropped_img_path,cropped_img)
            print('isPanelFound : '+isPanelFound)
            #return cropped_img_path
            # cv2.imshow('cropped_img',cropped_img)
            # cv2.waitKey(0)
            #retVal = IsScreenChanged(cropped_img_path,small_image)
            #print(retVal)  
            break
     return cropped_img_path
     #print('isPanelFound : '+isPanelFound)
     # cv2.namedWindow('output', cv2.WINDOW_NORMAL)  
     # cv2.imshow('output',large_image)
     # cv2.waitKey(0)

def IsScreenChanged(smallScreen_path,count,threshold,message):
        #ret_val = 2
        count = count +1
        #smallScreen_path = os.path.join(FAS001_ProgramScreens_path, small_img)
        newScreenShot = TakeScreenshot(count)
        newTemplatePath = ExtractTemplate_fromFullScreen(smallScreen_path,newScreenShot,count,threshold,message)  
        if(newTemplatePath == 'NOT_FOUND'):
            speak('Screen not changed Will compare screen again in 2 seconds')
            time.sleep(2)
            return IsScreenChanged(smallScreen_path,count,threshold,message)
        else:
            speak("Template found in screen shot given")
            #isItMatchingWithTemplate(smallScreen_path,newTemplatePath)
            comp_score = image_diff_V2.findScreenSimilarity(smallScreen_path,newTemplatePath)
            print('comp_score' + str(comp_score))
            if comp_score > 0.6: # If screen matches
                ret_val = "1"
                print('IF ' +str(ret_val))
                return "1"
            else:
                ret_val = "0"
                return "0"
                print('ELSE ' + str(comp_score))
        #return ret_val
            
        
       

def IsScreenChanged_old(PresentScreen,NextScreen,count):
    time.sleep(1)
    for small_img in os.listdir(FAS001_ProgramScreens_path):
        smallScreen_path = os.path.join(FAS001_ProgramScreens_path, small_img)
        IsProgramScreenpresent = findingImageinImage_v3(smallScreen_path,NextScreen,count)  
        print('IsProgramScreenpresent : '+str(IsProgramScreenpresent                ))
        if IsProgramScreenpresent == 1:
            if count > 5:
                return 100
            speak('Screen not changed Will compare screen again in 2 seconds')
            time.sleep(2)
            newScreenShot = TakeScreenshot(count+1)
            IsScreenChanged(PresentScreen,newScreenShot,count+1)
        else:
            return 0
                
             
def TakeScreenshot(count):
    myScreenshot = pyautogui.screenshot()
    filepath = r'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\FAS001_Screenshots\\000'+str(count)+'.jpg'
    myScreenshot.save(filepath)
    # print(filepath)
    return filepath


def ExecuteFirstSteps(assetNo):
    keyboard.write('1')
    keyboard.press_and_release('tab')
    keyboard.write(assetNo)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')


def ExceuteLastSteps():
    keyboard.press('shift')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.release('shift')

  
def ProcessTheSteps(PresentScreen):
   BPanel_Path = Process_B_Panel() 
   time.sleep(3)
   EPanel_Path = Process_E_Panel()
   FPanel_Path = Process_F_Panel()
   GPanel_Path = Process_G_Panel()
   Panel_2B_Path = Process_2B_Panel()
   Panel_3B_Path = Process_3B_Panel()
   Panel_4B_Path = Process_4B_Panel()
   Text_Panel = Process_Text_Panel()
   time.sleep(3)
   
def common_EnterMethod(template_path,count,threshold,message):
    time.sleep(2)
    speak('I am in panel '+message)
    print('I am in panel '+message)

    result = IsScreenChanged(template_path,count,threshold,message)
    if  result == "1": #Means it found the template
        speak('will process panel '+message+' Now')
        keyboard.press_and_release('enter')
    else:
        speak('score is not enough to process panel '+message)
    

def Process_B_Panel():
    template_B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_B.jpg'
    threshold = 0.3
    message = 'B'
    speak('I am in panel '+message)
    print('I am in panel '+message)
    
    result = IsScreenChanged(template_B,count,threshold,message)
    if  result == "1": #Means it found the template
        speak('will process panel '+message+' Now')
        keyboard.press_and_release('ctrl+5')
    else:
        speak('score is not enough to process panel '+message)
    
    
    
def Process_E_Panel():
    template_E=r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_E.jpg'
    threshold = 0.5
    common_EnterMethod(template_E,0,threshold,'E')
    
    
 
def Process_F_Panel():
    template_F = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_F.jpg'
    threshold = 0.5
    common_EnterMethod(template_F,0,threshold,'F')


def Process_G_Panel():
    template_G = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_G.jpg'
    threshold = 0.5
    common_EnterMethod(template_G,0,threshold,'G')


        
def Process_2B_Panel():
    template_2B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS002_B.jpg'
    threshold = 0.5
    result = IsScreenChanged(template_2B,0,threshold,'2B')
    if  result == "1": #Means it found the template
        speak('will process panel 2B Now')
        keyboard.press_and_release('F3')
        


def Process_3B_Panel():
    template_3B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS003_B.jpg'
    threshold = 0.5
    result = IsScreenChanged(template_3B,0,threshold,'3B')
    if  result == "1": #Means it found the template
        speak('will process panel 3B Now')
        keyboard.press_and_release('F3')
         
        
        
def Process_4B_Panel():
    template_4B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS004_B.jpg'
    threshold = 0.5
    result = IsScreenChanged(template_4B,0,threshold,'4B')
    if  result == "1": #Means it found the template
        speak('will process panel 4B Now')
        keyboard.press_and_release('F3')
        
 


def Process_Text_Panel():
    template_TB = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_TB.jpg'
    threshold = 0.5
    result = IsScreenChanged(template_TB,0,threshold,'text')
    if  result == "1": #Means it found the template
        speak('will process panel Text_Panel Now')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('enter')
        



print('What are you waiting for go to M3 screen..............')
speak('Going sleep now')
time.sleep(5)   # so that you can get time to move from command screen to M3 Screen
speak('Sleep is over')
for index,asset in enumerate(Assests):
    ExecuteFirstSteps(asset)
    # time.sleep(5)
    time.sleep(3)
    speak('Now I will display the asset')
    PresentScreen = TakeScreenshot(count)
    ProcessTheSteps(PresentScreen)
    speak('Now I will process Last steps')
    ExceuteLastSteps()



