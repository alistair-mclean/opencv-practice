import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('template.jpg', 0)
img2 = cv2.imread('match-image.jpg', 0)

# Initiate the SIFT detector
sift = cv2.SIFT() #DOES NOT WORK ANYMORE WITH OPENCV 3.0

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test
good = []
for m, n in matches:
	if m.distance < 0.75*n.distance:
		goood.append([m])

#cv2.drawMatchesKnn expects a list of lists as matches.
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, flags=2)

plt.imshow(img3), plt.show()

