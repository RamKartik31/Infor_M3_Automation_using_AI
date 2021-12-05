import cv2
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# im = Image.open('test_img.jpeg')
im = Image.open('8Pages.JPG') 
print(im.size)
# im.show()
image_file = im.convert('L')
# image_file.show()
#imsave('BW.png', image_file)


pix = im.load()
pix[10,19] = (255,0,0)
pix[10,36] = (255,0,0)
pix[10,53] = (255,0,0)
pix[10,74] = (255,0,0)
pix[10,91] = (255,0,0)
pix[10,114] = (255,0,0)
pix[10,126] = (255,0,0)
pix[10,150] = (255,0,0)
plt.imshow(im)
plt.show()