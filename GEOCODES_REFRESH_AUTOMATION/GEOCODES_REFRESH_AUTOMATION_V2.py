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
import image_difference
#import mysql.connector
import pyodbc 
'''
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'CUSPXK2F.carcgl.com\M3SQLBE1DEV,3433'
# server = 'CCAMQA1F.carcgl.com\\M3SQLBE1PRD,1433'
database = 'M3FDBDEV' 
username = 'MDBUSR' 
password = 'D3VMdbU$3r' 
conStr = 'DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
#print(conStr)

cnxn = pyodbc.connect(conStr)
cursor = cnxn.cursor()
'''

Customer_nos = ['SC08367','SC08367','SC01196','SC01196','SC01257','SC32422','SC32422','SC32426','SC32426','SC32427','SC32427','SC13990','SC22752']
Atp_nos = ['2','2','2','2','2','1','2','1','2','1','2','2','2']
Address_nos = ['548','549','10120','10121','454','S001  ','1','S001  ','1','S001  ','1','424','24']


def GET_SPOT_BLANK_GEOCODES():
    strSQL_GET_SPOT_BLANK_GEOCODES = "select OPCONO,OPCUNO,OPADRT,OPADID,OPCUNM,OPGEOC,OPRGDT from MVXJDTA.OCUSAD WHERE OPCONO = 910 AND OPADRT <= 2 AND LEN(OPGEOC) < 2"
    SPOT_BLANK_GEOCODES_DATA = cursor.execute(strSQL_GET_SPOT_BLANK_GEOCODES) 
    print(type(SPOT_BLANK_GEOCODES_DATA)) 
    for row in SPOT_BLANK_GEOCODES_DATA:
        Customer_nos.append(row[1])
        Atp_nos.append(str(int(row[2])))
        Address_nos.append(row[3])
        # print("OPCUNO = ", row[1] )
        # print("OPADRT  = ", row[2])
        # print("OPADID  = ", row[3], "\n")
    
    
# GET_SPOT_BLANK_GEOCODES()
print('SPOT_BLANK_GEOCODES_DATA')
print(Customer_nos)
print(type(Customer_nos)) 
print(Atp_nos)
print(type(Atp_nos)) 
print(Address_nos)
print(type(Address_nos)) 



count = 0

PresentScreen_Data = []
NextScreen_Data = []


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
            cropped_img_path = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\M3\\GEOCODES_REFRESH_AUTOMATION\\CRS610_CroppedScreens\\cropped_img_'+str(count)+'.jpg'
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
            comp_score = image_difference.findScreenSimilarity(smallScreen_path,newTemplatePath)
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
    filepath = r'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\M3\\GEOCODES_REFRESH_AUTOMATION\\CRS610_Screenshots\\000'+str(count)+'.jpg'
    myScreenshot.save(filepath)
    # print(filepath)
    return filepath
    
    
    
def ExecuteFirstSteps(Customer_no):
    speak('Searching Customer_no')
    keyboard.write(Customer_no)
    keyboard.press_and_release('enter')
    time.sleep(5)
    speak('Selecting addresses')
    keyboard.press_and_release('tab')



def ExecuteLastSteps():
    keyboard.press('shift')
    keyboard.press_and_release('tab')
    keyboard.release('shift')



def ProcessTheSteps(Atp_no,address_no):
   Process_B_Panel() 
   time.sleep(3)
   Process_2B_Panel(Atp_no,address_no)
   Process_2E_Panel()
   Process_2F_Panel()
   time.sleep(5)
   Process_2F_Panel() # CALLING 2f PANEL AGAIN AS GEOCODE WILL REFRESH..
   Process_Text_Panel()
   Closing_2B_Panel()
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
        next_button_int_tuple =  pyautogui.locateOnScreen('close.jpg', confidence=0.7)
        print('next_button_int_tuple: '+str(next_button_int_tuple))
        next_button_int_coordinates = pyautogui.center(next_button_int_tuple)
        print('next_button_int_coordinates: '+str(next_button_int_coordinates))
        pyautogui.click(next_button_int_coordinates)
    else:
        speak('score is not enough to process panel '+message)
        
        
        
def Process_B_Panel():
    template_B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\M3\GEOCODES_REFRESH_AUTOMATION\CRS610_ProgramScreens\CRS610_B.jpg'
    threshold = 0.3
    message = 'B'
    speak('I am in panel '+message)
    print('I am in panel '+message)
    
    result = IsScreenChanged(template_B,count,threshold,message)
    if  result == "1": #Means it found the template
        speak('will process panel '+message+' Now')
        keyboard.press('ctrl')
        keyboard.press_and_release('1')
        keyboard.press_and_release('1')
        keyboard.release('ctrl')
    else:
        speak('score is not enough to process panel '+message)
        
        
        
def Process_2B_Panel(Atp_no,address_no):
    template_2B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\M3\GEOCODES_REFRESH_AUTOMATION\CRS610_ProgramScreens\CRS610_2B.jpg'
    threshold = 0.5
    message = '2B'
    speak('I am in panel '+message)
    print('I am in panel '+message)
    
    result = IsScreenChanged(template_2B,count,threshold,message)
    # speak('Searching address')
    if  result == "1": #Means it found the template
        speak('will process panel 2B Now')
        # keyboard.write('2')
        keyboard.write(Atp_no)
        keyboard.press_and_release('tab')
        keyboard.write(address_no)
        keyboard.press_and_release('enter')
        speak('Searching address')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        speak('Checking geocode')
        keyboard.press_and_release('ctrl+2')
    else:
        speak('score is not enough to process panel '+message)

       
def Process_2E_Panel():
    template_2E = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\M3\GEOCODES_REFRESH_AUTOMATION\CRS610_ProgramScreens\CRS610_2E.jpg'
    threshold = 0.3
    message = '2E'
    common_EnterMethod(template_2E,count,threshold,message)
        
        
def Process_2F_Panel():
    template_2F = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\M3\GEOCODES_REFRESH_AUTOMATION\CRS610_ProgramScreens\CRS610_2F.jpg'
    threshold = 0.5
    message = '2F'
    common_EnterMethod(template_2F,count,threshold,message)
        
        
def Process_Text_Panel():
    template_TB = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\M3\GEOCODES_REFRESH_AUTOMATION\CRS610_ProgramScreens\CRS610_TB.jpg'
    threshold = 0.5
    result = IsScreenChanged(template_TB,0,threshold,'text')
    if  result == "1": #Means it found the template
        speak('will process Text Panel Now')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('enter')
    else:
        speak('score is not enough to process panel '+message)
        
        
def Closing_2B_Panel():
    template_2B = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\M3\GEOCODES_REFRESH_AUTOMATION\CRS610_ProgramScreens\CRS610_2B.jpg'
    threshold = 0.5
    message = '2B'
    common_CloseMethod(template_2B,count,threshold,message)



        
print('What are you waiting for go to M3 screen..............')
speak('Going sleep now')
time.sleep(5)   # so that you can get time to move from command screen to M3 Screen
speak('Sleep is over')
for index1,Customer_no in enumerate(Customer_nos):
    Atp_no = Atp_nos[index1]
    address_no = Address_nos[index1]
    ExecuteFirstSteps(Customer_no)
    time.sleep(3)
    ProcessTheSteps(Atp_no,address_no)
    speak('Now I will process Last steps')
    ExecuteLastSteps()