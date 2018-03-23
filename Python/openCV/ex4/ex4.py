import cv2
import numpy as np

img = cv2.imread('pro.png', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

px = img[55, 55]
img[100:150, 100:150] = [255, 255, 255]

my_face = img[250:400, 250:400]

img[0:150, 0:150] = my_face

# ROI - Region of Image 
roi = img[100:150, 100:150]
cv2.imshow('image', img)
cv2.imwrite('output.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
