import cv2
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# im = Image.open('test_img.jpeg')
im = Image.open('8Pages.JPG') 

# im.show()
image_file = im.convert('L')
# image_file.show()
#imsave('BW.png', image_file)


pix = im.load()
# pix[189,186,181] = (255,0,0)
# pix.show()
#print(im.size()) # Get the width and hight of the image for iterating over
# print(pix[10,10]) 
pix_val = []

def findPage(index):
    print('Hello')
    plt.plot(10, i, marker='.', color="red")
    plt.imshow(im)
    plt.show()
    
i = 0
while i<100:
    # print(pix[10,i])
    if pix[10,i] == (194,189,183):
        print(i)
        findPage(i)
    if pix[10,i] == (190,190,182):
        print(i)
        findPage(i)
    if pix[10,i] == (204,203,198):
        print(i)
        findPage(i)
    if pix[10,i] == (161,160,155):
        print(i)
        findPage(i)
    if pix[10,i] == (174,173,168):
        print(i)
        findPage(i)
    pix_val.append(pix[10,i])
    # print('hi')
    # print(type(pix[10,i]))
    i=i+1

# im.show()
# print(pix_val)
'''
image = cv2.imread('test_img.jpeg')
 
height = image.shape[0]
width = image.shape[1]

print(height)
print(width)
 
cv2.line(image, (10,10), (10,height), (255,0,0), 2)
# cv2.line(image, (0,0), (width, height), (0,0,255), 12)

cv2.imshow("Image", image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
'''