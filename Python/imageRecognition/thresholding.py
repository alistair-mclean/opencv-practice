from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



# Define a threshold array which holds the mean of 
# each pixel in each image. 
def threshold(imageArray):
	balanceAr = []
	newAr = imageArray

	for eachRow in imageArray:
		for eachPix in eachRow:
			avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
			balanceAr.append(avgNum)

	balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
	for eachRow in newAr:
		for eachPix in eachRow:
			if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				eachPix[3] = 255
			else:
				eachPix[0] = 0
				eachPix[1] = 0
				eachPix[2] = 0
				eachPix[3] = 255
	return newAr

# Load the images as arrays
i = Image.open('images/numbers/0.1.png')
i.setflags(write) = true
iar = np.asarray(i)
i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.asarray(i2)
i2.setflags(write) = true
i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.asarray(i3)
i3.setflags(write) = true
i4 = Image.open('images/sentdex.png')
iar4 = np.asarray(i4)
i4.setflags(write) = true


# Threshold the images
iar = threshold(iar)
iar2 = threshold(iar2)
iar3 = threshold(iar3)
iar4 = threshold(iar4)

# Create a new figure to contain plots of all of the 
# images in our array. 
fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

# Display the plots on the figure
ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)
plt.show()