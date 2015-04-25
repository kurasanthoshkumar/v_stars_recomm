import numpy as np
import cv2
import argparse
import os

def get_body(filepath):
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    max_w=0
    max_h=0
    max_x=0
    max_y=0

    for (x,y,w,h) in faces:
        if (w * h) > (max_w * max_h):
            max_w = w
            max_h = h
            max_x = x
            max_y = y
   
    print max_x,max_y,max_h,max_w
 
    if (max_w > 0):
        body = img[max_y+max_h:max_y+max_h+(4*max_h), max_x-max_w:max_x+max_w+max_w]
        cv2.imwrite("/tmp/"+os.path.splitext(os.path.basename(filepath))[0]+"_trim.jpg",body)
        return "/tmp/"+os.path.splitext(os.path.basename(filepath))[0]+"_trim.jpg"

    else:
        cv2.imwrite("/tmp/"+os.path.splitext(os.path.basename(filepath))[0]+"_trim.jpg",img)
        return "/tmp/"+os.path.splitext(os.path.basename(filepath))[0]+"_trim.jpg"
