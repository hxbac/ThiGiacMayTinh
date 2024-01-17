# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:10:34 2023

@author: Duy Hao
"""

import  cv2
img = cv2.imread('../anh.jpg')

img_blur = cv2.GaussianBlur(img, (7,7),0)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img_gray, cv2.CV_64F)
img_lap = cv2.convertScaleAbs(lap)
cv2.imshow('Laplacian', img_lap)
cv2.waitKey(0)
cv2.destroyAllWindows()