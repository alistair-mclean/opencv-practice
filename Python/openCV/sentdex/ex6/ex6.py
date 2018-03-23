import numpy as np
import cv2
# INCREASING THE BRIGHTNESS OF A 


img = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
ret2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
ret3, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_OTSU)


#INCREASING THE BRIGHTNESS OF AN IMAGE
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v += 50
final_hsv = cv2.merge((h, s, v))
cv2.imshow('final_hsv', final_hsv)
img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("image_processed.jpg", img)

# Apply an adaptive gaussian threshold to a gray scaled image to make a very dark image visible 
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow('og', img)
cv2.imshow('thrsh', threshold)
cv2.imshow('gray', threshold2)
cv2.imshow('gaus', gaus)


cv2.waitKey(0)
cv2.destroyAllWindows()