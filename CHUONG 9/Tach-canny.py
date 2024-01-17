# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:50:53 2023

@author: Duy Hao
"""

import cv2
img = cv2.imread('../anh.jpg')

angle = 1
def get_canny(pos):
    global angle
    angle = pos
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Trackbar')
cv2.createTrackbar('Tach bien','Trackbar',0,255,get_canny)
while True:
    new_img = cv2.Canny(img_gray,angle, angle*2)
    cv2.imshow('Trackbar',new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()