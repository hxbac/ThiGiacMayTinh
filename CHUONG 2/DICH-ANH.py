# -*- coding: utf-8 -*-
"""
Created on Mon May 22 10:40:37 2023

@author: Duy Hao
"""

import cv2
import numpy as np
img = cv2.imread('../anh.jpg')
w,h = img.shape[:2]

fx = 1
fy = 1
def get_fx(pos):
    global fx
    fx = pos
def get_fy(pos):
    global fy
    fy = pos

cv2.namedWindow('Trackbar')
cv2.createTrackbar('fx','Trackbar', 0, 255, get_fx)
cv2.createTrackbar('fy','Trackbar', 0 ,255, get_fy)
while True:
    array = np.array([[1,0,fx],[0,1,fy]], dtype = np.float32)
    new_img = cv2.warpAffine(img,array,(h,w))
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()