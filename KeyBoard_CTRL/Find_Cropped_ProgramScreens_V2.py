import cv2
import os
import numpy as np

method = cv2.TM_SQDIFF_NORMED

FullScreens_Path = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\FAS001_FullScreens\\'
ProgramScreens_Path = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\FAS001_ProgramScreens\\'
CroppedScreens_Path = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\KeyBoard_CTRL\\FAS001\\FAS001_CroppedScreens\\000'

def findingImageinImage_v2(small_image,large_image):
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(small_image)
    large_image = cv2.imread(large_image)

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    cv2.imshow('output',large_image)

    # The image is only displayed if we call this
    cv2.waitKey(0)

def findingImageinImage(small_image,large_image,method,count):
    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    image = cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    cropped_image = image[MPy:MPy+trows,MPx:MPx+tcols]
    # Saving rectangle image
    
    CroppedScreen_Img = CroppedScreens_Path+ str(count)+ '.jpg'
    cv2.imwrite(CroppedScreen_Img, cropped_image)

    # Display the original image with the rectangle around the match.
    cv2.imshow('output',image)

    # The image is only displayed if we call this
    cv2.waitKey(0)

small_image = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_E.jpg'
large_image = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_FullScreens\FAS001_B1.jpg'

findingImageinImage_v2(small_image,large_image)

small_image = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_E.jpg'
large_image = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_FullScreens\FAS001_E.jpg'

findingImageinImage_v2(small_image,large_image)

small_image = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_ProgramScreens\FAS001_E.jpg'
large_image = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_FullScreens\FAS001_F.jpg'

findingImageinImage_v2(small_image,large_image)