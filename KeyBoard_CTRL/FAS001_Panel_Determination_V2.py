import cv2
import os
import numpy as np
import pytesseract
import speech_recognition as sr
import pyttsx3
import image_diff_V2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# method = cv2.TM_SQDIFF_NORMED
# method = cv2.TM_CCOEFF_NORMED

def IsScreenChanged(cropped_img_path,small_image_p):
    # time.sleep(1)
    SSIM_Score = image_diff_V2.findScreenSimilarity(cropped_img_path,small_image_p)
    if SSIM_Score > 0.8:
        return 1
    else:
        return 0

def findingImageinImage_v3(small_image_p_in,large_image_p_in): #better method than v2
     isPanelFound = 'No'    
     method = cv2.TM_CCOEFF_NORMED
     # Read the images from the file
     small_image = cv2.imread(small_image_p_in)
     large_image = cv2.imread(large_image_p_in)
     
     w,h = small_image.shape[:2]
     
     res = cv2.matchTemplate(large_image,small_image,method)
     
     threshold = 0.5
     # print('res'+str(res))
     
     loc= np.where(res >= threshold)
     
     for pt in zip(*loc[::-1]):
        isPanelFound = 'Yes'
        cv2.rectangle(large_image,pt,(pt[0]+h,pt[1]+w),(0,0,255),2)
        if isPanelFound == 'Yes':
            cropped_img = large_image[pt[1]:pt[1]+w,pt[0]:pt[0]+h]
            cropped_img_path = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\cropped_img.jpg'
            cv2.imwrite(cropped_img_path,cropped_img)
            cv2.imshow('cropped_img',cropped_img)
            cv2.waitKey(0)
            retVal = IsScreenChanged(cropped_img_path,small_image_p)
            print(retVal)
            break
        # print('pt')
        # print(pt[0])
     print('isPanelFound : '+isPanelFound)
     cv2.namedWindow('output', cv2.WINDOW_NORMAL)  
     cv2.imshow('output',large_image)
     cv2.waitKey(0)

def findingImageinImage_v2(small_image_p_in,large_image_p_in):
    method = cv2.TM_SQDIFF_NORMED
   
    # Read the images from the file
    small_image = cv2.imread(small_image_p_in)
    large_image = cv2.imread(large_image_p_in)
    print(large_image.shape)
    #cv2.namedWindow("large_image", cv2.WINDOW_NORMAL)  
    #cv2.imshow('large_image',large_image)
    #cv2.waitKey(0)
    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    # mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    # min_v, max_v, min_pt, max_pt = cv2.minMaxLoc(res)
    min_v, max_v, min_pt, max_pt = cv2.minMaxLoc(result)
    # print('minimum squared difference')
    print(max_v)

    # Draw the rectangle: Extract the coordinates of our best match
    # MPx,MPy = mnLoc
    MPx,MPy = min_pt
      
    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]
    #print(trows,tcols)
    print('Rectangle coordinates')
    print(MPx,MPy)
    print(MPx+tcols,MPy+trows)
    cropped_img = large_image[MPy:MPy+trows,MPx:MPx+tcols]
    cv2.imwrite('C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\cropped_img.jpg',cropped_img)
    print('cropped_img.JPG-----------------------------------------------------------------------------------------------------------')
    print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\cropped_img.jpg'))
    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)  
    cv2.imshow('output',large_image)

    # The image is only displayed if we call this
    cv2.waitKey(0)

def findingImageinImage(small_image,large_image):
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(small_image)
    large_image = cv2.imread(large_image)

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    # print(mn,_,mnLoc,_)

    # Draw the rectangle: Extract the coordinates of our best match
    MPx,MPy = mnLoc
    #print(MPx,MPy)

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]
   
    # Step 3: Draw the rectangle on large_image
    
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    cv2.imshow('output',large_image)

    # The image is only displayed if we call this
    cv2.waitKey(0)

# small_images_path = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens'
small_image_p = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_G.jpg'
large_image_p = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_FullScreens\FAS001_G.jpg'
#blank_image_p = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_FullScreens\Blank.jpg'
#large_image=blank_image_p

findingImageinImage_v3(small_image_p,large_image_p)
#findingImageinImage_v2(small_image_p,large_image_p)
'''
blank_image = cv2.imread(blank_image_p)
cv2.rectangle(blank_image, (1941,1110),(2699,1560),(0,0,255),2)
#cv2.rectangle(blank_image, (524,580),(1282,1030),(0,255,0),2)
cv2.imshow('output',blank_image)
cv2.waitKey(0)
'''
'''
for small_img in os.listdir(small_images_path):
    smallScreen_path = os.path.join(small_images_path, small_img)
    print(smallScreen_path)

    findingImageinImage_v2(smallScreen_path,large_image)
'''