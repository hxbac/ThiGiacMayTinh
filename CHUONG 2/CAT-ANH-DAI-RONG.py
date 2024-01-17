# -*- coding: utf-8 -*-
"""
Created on Mon May 22 10:14:45 2023

@author: Duy Hao
"""

import cv2
img = cv2.imread('../anh.jpg')
h,w = img.shape[:2]
left = 0
bottom = 0
top = int(input('Nhap chieu cao: '))
right = int(input('Nhap chieu rong: '))
img_drop = img[bottom:top, left:right]
cv2.imshow('anh cat', img_drop)
cv2.waitKey(0)
cv2.destroyAllWindows()