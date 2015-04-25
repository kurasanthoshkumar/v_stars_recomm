# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)

	print "MSE = " + str(m)
	print "SSIM = " + str(s)
	return
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()


i1 = cv2.imread("images/1.jpg")
i2 = cv2.imread("images/2.jpg")
i3 = cv2.imread("images/3.jpg")
i4 = cv2.imread("images/4.jpg")
p1 = cv2.imread("images/p1.jpg")
 
# convert the images to grayscale
i1 = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY)
i2 = cv2.cvtColor(i2, cv2.COLOR_BGR2GRAY)
i3 = cv2.cvtColor(i3, cv2.COLOR_BGR2GRAY)
i4 = cv2.cvtColor(i4, cv2.COLOR_BGR2GRAY)
p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2GRAY)

compare_images(i1, p1)
compare_images(i2, p1)
compare_images(i3, p1)
compare_images(i4, p1)
