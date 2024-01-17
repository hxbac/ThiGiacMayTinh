# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:57:00 2023

@author: Duy Hao
"""

import cv2
img = cv2.imread('../anh.jpg')
angle = 1
w,h = img.shape[:2]
def get_angle(pos):
    global angle
    angle = -pos

cv2.namedWindow('Trackbar')
cv2.createTrackbar('Rotation','Trackbar',0,360,get_angle)

while True:
    M = cv2.getRotationMatrix2D((w / 2, h / 2),angle, 1)
    new_img = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()