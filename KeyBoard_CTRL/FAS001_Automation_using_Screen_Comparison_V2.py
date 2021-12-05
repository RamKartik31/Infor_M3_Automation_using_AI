# THIS IS A WORKING AUTOMATION CODE USING BOTH KEYBOARD AND MOUSE
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

# Assests = ['5480','5480','9983']
Assests = ['25651','35951','38635','38636','38726','38882','39946','40050','40051','41798','41800','41802','41804','41836','41854','42283','42284','42579','42580','43509','43510','43513','43514','43515','43516','43649','43652','43894','43937','43940','43941','44158','44159','44160','44335','44432','44544','44828','44951','44952','44953','44954','44955','44956','45252','45458','45459','45466','45469','45470','45471','45472','45473','45474','45476','45477','45502','45503','45504','45511','45512','45513','45514','45515','45516','45544','45545','45555','45556','45557','45558','45987','45988','45990','45991','45992','45993','45994','45995','45996','45999','46004','46005','46006','46007','46008','46010','46015','46017','46019','46027','46031','46033','46042','46043','46044','46068','46069','46129','46130','46132','46328','46429','46430','46431','46476','46483','46484','46486','46487','46488','46489','46492','46495','46508','46510','46511','46512','46513','46514','46558','46639','46646','46647','46648','46652','46653']

count = 0

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
   Process_B_Panel() 
   time.sleep(3)
   Process_E_Panel()
   Process_F_Panel()
   Process_G_Panel()
   Process_2B_Panel()
   Process_3B_Panel()
   Process_4B_Panel()
   Process_Text_Panel()
   time.sleep(3)
   
def common_EnterMethod(template_path,count,threshold,message):
    time.sleep(2)
    speak('I am in panel '+message)
    print('I am in panel '+message)

    result = IsScreenChanged(template_path,count,threshold,message)
    if  result == "1": #Means it found the template
        speak('will process panel '+message+' Now')
        # keyboard.press_and_release('enter')
        next_button_int_tuple =  pyautogui.locateOnScreen('next.jpg', confidence=0.9)
        print('next_button_int_tuple: '+str(next_button_int_tuple))
        next_button_int_coordinates = pyautogui.center(next_button_int_tuple)
        print('next_button_int_coordinates: '+str(next_button_int_coordinates))
        pyautogui.click(next_button_int_coordinates)
    else:
        speak('score is not enough to process panel '+message)
    
def common_CloseMethod(template_path,count,threshold,message):
    time.sleep(2)
    speak('I am in panel '+message)
    print('I am in panel '+message)

    result = IsScreenChanged(template_path,count,threshold,message)
    if  result == "1": #Means it found the template
        speak('will process panel '+message+' Now')
        # next_button_int_tuple =  pyautogui.locateOnScreen('close.jpg', confidence=0.9)
        close_button_int_tuple =  pyautogui.locateOnScreen('close.jpg', confidence=0.7)
        print('close_button_int_tuple: '+str(next_button_int_tuple))
        close_button_int_coordinates = pyautogui.center(close_button_int_tuple)
        print('close_button_int_coordinates: '+str(close_button_int_coordinates))
        pyautogui.click(close_button_int_coordinates)
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
        # pyautogui.click(button='right')
    else:
        speak('score is not enough to process panel '+message)
    
    
    
def Process_E_Panel():
    template_E=r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_E.jpg'
    threshold = 0.3
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
    common_CloseMethod(template_2B,count,threshold,'2B')
        


def Process_3B_Panel():
    template_3B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS003_B.jpg'
    threshold = 0.5
    common_CloseMethod(template_3B,count,threshold,'3B')
         
        
        
def Process_4B_Panel():
    template_4B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS004_B.jpg'
    threshold = 0.5
    common_CloseMethod(template_4B,count,threshold,'4B')
        
 

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



