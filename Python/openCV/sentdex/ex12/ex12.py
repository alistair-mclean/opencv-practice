import cv2
import numpy as np
import matplotlib.pyplot as plt 

# CORNER DETECTION

img = cv2.imread('img2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# CONVERT TO FLOAT32 TO SATISFY THE CORNER DETECTION AGLO
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # (on what, how many, img quality, minimum distance between each corner)
corners = np.int0(corners)

for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('Corner', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

