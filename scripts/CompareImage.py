# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

class CompareImage:
	def __init__(self):
		print "Initialized CompareImage"

	def _mse(self, imageA, imageB):
		# the 'Mean Squared Error' between the two images is the
		# sum of the squared difference between the two images;
		# NOTE: the two images must have the same dimension
		err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
		err /= float(imageA.shape[0] * imageA.shape[1])
	
		# return the MSE, the lower the error, the more "similar"
		# the two images are
		return err

	
	def get_mse(self, imagePath1, imagePath2):
		i1 = cv2.imread(imagePath1)
		i2 = cv2.imread(imagePath2)
		
		# convert the images to grayscale
		i1 = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY)
		i2 = cv2.cvtColor(i2, cv2.COLOR_BGR2GRAY)
		
		m = self._mse(i1, i2)
		return m

#ci = CompareImage()
#print ci.get_mse("images/142338.jpg", "images/482351.jpg")	
