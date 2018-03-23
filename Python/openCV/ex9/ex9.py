import numpy as np
import cv2 

# EDGE DETECTION 


cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	# Laplacian blur
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)

	# Sobel blur
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
	
	# CANNY EDGE DETECTION
	edges = cv2.Canny(frame, 80, 80)

	cv2.imshow('original', frame)
	cv2.imshow('laplacian', laplacian)
	cv2.imshow('sobelx', sobelx)
	cv2.imshow('sobely', sobely)
	cv2.imshow('edges', edges)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()