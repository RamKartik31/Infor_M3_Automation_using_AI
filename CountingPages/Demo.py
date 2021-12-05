import cv2

from PIL import Image

im = Image.open('test_img.jpeg') 
im.show()
image_file = im.convert('L')
image_file.show()
#imsave('BW.png', image_file)


pix = im.load()
#print(im.size()) # Get the width and hight of the image for iterating over
print(pix[10,10]) 
pix_val = []

i = 0
while i<1000:
    print(pix[10,i])
    pix_val.append(pix[10,i])
    # print(type(pix[10,i]))
    i=i+1

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