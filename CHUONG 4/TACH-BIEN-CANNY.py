# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:21:55 2023

@author: Duy Hao
"""

import cv2
img = cv2.imread('../anh.jpg')

img_blur = cv2.GaussianBlur(img, (7,7),0)
img_gray = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY )
img_canny = cv2.Canny(img_gray,100,200)
cv2.imshow('cannhy',img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()