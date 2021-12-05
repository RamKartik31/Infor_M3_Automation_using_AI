import cv2

# read the image file
# img = cv2.imread('8Pages.JPG', 2)
# img = cv2.imread('72Pages.jpeg', 2)
# img = cv2.imread('36Pages.PNG', 2)
img = cv2.imread('test_img.jpeg', 2)


ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
