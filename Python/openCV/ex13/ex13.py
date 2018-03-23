import cv2
import numpy as np
import matplotlib.pyplot as plt

# FEATURE MATCHING (BRUTE FORCE METHOD)

img1 = cv2.imread('template.jpg', 0)
img2 = cv2.imread('match-image.jpg', 0)

# SIFT - SCALE INVARIANTE FEATURE TRANSFORM 
# Initiate the SIFT detector
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Create the Brute Force Matcher object 
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

plt.imshow(img3), plt.show()
