import cv2
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt


# im_cv2 = cv2.imread('8Pages.JPG')
im_cv2 = cv2.imread('72Pages_Full.jpeg')


# originalImage = cv2.imread('8Pages.JPG')
originalImage = cv2.imread('72Pages_Full.jpeg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 220, cv2.THRESH_BINARY)
 
cv2.imshow('Original image',originalImage)
cv2.waitKey(0)
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.waitKey(0)


# im = Image.open('8Pages.JPG') 
im = Image.open('72Pages_Full.jpeg') 
im.show()

im_BW = im.convert('1')
im_BW.show()

print(im_cv2.shape)
height = im_cv2.shape[0]
print(im_cv2.shape[0])
cv2.line(im_cv2, (10,0), (10, height), (0,0,255), 2)

pix = im.load()
i=0
while i<height:
    print(pix[10,i])
    i=i+1
    
cv2.imshow('im',im_cv2)
cv2.waitKey(0)


