#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:44:35 2020

@author: ali
"""

import os
import cv2
import numpy as np

#find working directory
retval = os.getcwd()
print ("Current working directory %s" % retval)



cv2.namedWindow("preview")
vc = cv2.VideoCapture('http://192.168.0.111:4747/video')
#vc = cv2.VideoCapture('testfiles/11.mp4')
#image = cv2.imread('./testfiles/camsave0.bmp')
#gray = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2GRAY)
#cv2.imwrite('./testfiles/graysave.bmp', gray)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

i = 0
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    #print (type (frame))
    gray = cv2.cvtColor(np.asarray(frame), cv2.COLOR_BGR2GRAY)   #change RGB to gray format
    reimage = cv2.resize(gray, (64, 48))   #resize image
    if cv2.imwrite('./testfiles/camsave' + str(i) + '.bmp', reimage): #save the gray image in .bmp format
        print ('camsave' , i)
        #print (gray.shape)   #check the channels of grayscale
        #np.savetxt("./testfiles/img_pixels1.csv", reimage, delimiter=',')   #save image as .csvfile
        raveled = reimage.ravel()  #make a 1-dimensional view of image
        np.savez('./testfiles/npzfiles/img_pixels' + str(i) + '.npz', img = raveled, order = i)  #save as a .npz file
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    i += 1
cv2.destroyWindow("preview")




