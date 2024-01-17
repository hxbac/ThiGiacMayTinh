# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:51:19 2023

@author: Duy Hao
"""

import cv2

img = cv2.imread('../anh.jpg')

h,w = img.shape[:2]
rotate  = 0
def get_rotate(pos):
    global rotate
    rotate = pos
cv2.namedWindow('Trackbar')
cv2.createTrackbar('gsfg', 'Trackbar',0, 360, get_rotate)
while True:
    M = cv2.getRotationMatrix2D((h/2, w/2),rotate,1)
    new_img = cv2.warpAffine(img, M,(h,w))
    cv2.imshow('Trackbar', new_img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()
    