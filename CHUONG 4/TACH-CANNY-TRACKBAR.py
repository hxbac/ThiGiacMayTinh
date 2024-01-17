# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:28:31 2023

@author: Duy Hao
"""

import cv2
img = cv2.imread('../anh.jpg')
underX = 1
def get_underX(pos):
    global underX
    underX = pos
    
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Trackbar')
cv2.createTrackbar('Canny','Trackbar',0,255,get_underX)
while True:
    new_img = cv2.Canny(img_gray,underX,underX * 3)
    cv2.imshow('Trackbar',new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()