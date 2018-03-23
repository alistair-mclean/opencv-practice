import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread('test1.jpg', cv2.IMREAD_GRAYSCALE) #convert to grayscale for speed of processing
#IMREAD_GRAYSCALE: 0
#IMREAD_COLOR: 1
#IMREAD_UNCHANGED: -1

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100], [80,100], 'c', linewidth=5)
plt.plot([10,100], [10, 300], 'r', linewidth=2)

#cv2.imwrite('grayTest1.jpg', img)

plt.show()


