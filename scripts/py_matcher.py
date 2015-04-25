import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

def get_number_of_matches(image1,image2):
    img1 = cv2.imread(image1,0)          # queryImage
    img2 = cv2.imread(image2,0) # trainImage
    sift = cv2.Feature2D_create('SIFT')
 # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
             good.append([m])
    return_list =[]
    return_list.append(len(matches))
    return_list.append(len(good))
    return return_list

if __name__ == '__main__':
    print get_number_of_matches(sys.argv[1],sys.argv[2])    
