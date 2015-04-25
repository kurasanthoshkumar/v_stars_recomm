# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import Image
import random
import os

class CompareImage:
	reqImgWidth=180
	reqImgHeight=240
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
		resizedImage1 = self.resizeImage(imagePath1, self.reqImgWidth, self.reqImgHeight)
		resizedImage2 = self.resizeImage(imagePath2, self.reqImgWidth, self.reqImgHeight)
		
		if resizedImage1 == None or resizedImage1 == None:
			return None

		print resizedImage1
		print resizedImage2
		i1 = cv2.imread(resizedImage1)
		i2 = cv2.imread(resizedImage2)
		
		# convert the images to grayscale
		i1 = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY)
		i2 = cv2.cvtColor(i2, cv2.COLOR_BGR2GRAY)
		
		m = self._mse(i1, i2)
		return m


	def resizeImage(self, imagePath, width, height):
		outfile=imagePath+"_"+str(width)+"_"+str(height)
		if not os.path.isfile(imagePath):
			print imagePath + " does not exist"
			return None

		#if resized file already exists, return the same
		if os.path.isfile(outfile):
			return outfile

		try:
			im = Image.open(imagePath)		
			if im.size[0]==self.reqImgWidth and im.size[1]==self.reqImgHeight:
				return imagePath
            		im.thumbnail((width,height), Image.ANTIALIAS)
            		im.save(outfile, "JPEG")
			return outfile
		except IOError:
			print "IOError while resizing " + imagePath
			return None
		
#ci = CompareImage()
#print ci.resizeImage("images/p1.jpg", 180, 240)
#print ci.get_mse("images/142338.jpg", "images/p1.jpg")	

