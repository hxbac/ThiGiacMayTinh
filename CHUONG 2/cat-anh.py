# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:24:54 2023

@author: Duy Hao
"""

import cv2
img = cv2.imread('../anh.jpg')
h,w = img.shape[:2]
x1 = int(input('Nhap toa do x1:'))
y1 = int(input('Nhap toa do y1:'))
x2 = int(input('Nhap toa do x2:'))
y2 = int(input('Nhap toa do y2:'))

img_drop = img[y1:y2, x1:x2]
cv2.imshow('á', img_drop)
cv2.waitKey=(0)
cv2.destroyAllWindows()