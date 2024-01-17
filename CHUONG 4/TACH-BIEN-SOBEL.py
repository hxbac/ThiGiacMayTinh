# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:28:22 2023

@author: Duy Hao
"""

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('../anh.jpg')
img_blur = cv2.GaussianBlur(img,(7,7),0)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
grad_x = cv2.Sobel(img_gray,cv2.CV_64F,1,0,3 )
grad_y = cv2.Sobel(img_gray,cv2.CV_64F, 0,1,3)
cvtX = cv2.convertScaleAbs(grad_x)
cvtY = cv2.convertScaleAbs(grad_y)
img_sobel = cv2.addWeighted(cvtX,0.5,cvtY,0.5,0)
cv2.imshow('Sobel', img_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()