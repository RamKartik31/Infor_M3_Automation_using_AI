from PIL import Image, ImageEnhance
import cv2

'''
#im = Image.open('test_img.jpeg')
#im.show()
enhancer = ImageEnhance.Sharpness(im)
#enhancer.show()

enhancer2 = enhancer.enhance(2)
#enhancer2.show()

enhancer10 = enhancer.enhance(10)
#enhancer10.show()
'''

image_path = 'test_img.jpeg'
image_path='8Pages.JPG'
image_path = '72Pages.jpeg' 
im_cv2 = cv2.imread(image_path)
height = im_cv2.shape[0]
cv2.line(im_cv2, (10,0), (10, height), (0,0,255), 2)

cv2.imshow('im',im_cv2)
cv2.waitKey(0)

im = Image.open(image_path) 
pix = im.load()
i=0
while i<height:
    print(pix[10,i])
    i=i+1
