# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:34:37 2023

@author: Duy Hao
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../anh.jpg')
img_blur = cv2.GaussianBlur(img, (1,1),0)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
grad_x = cv2.Sobel(img_gray, cv2.CV_64F, 1,0,3)
grad_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1,3)
cvtX = cv2.convertScaleAbs(grad_x)
cvtY = cv2.convertScaleAbs(grad_y)
img_sobel = cv2.addWeighted(cvtX,0.5,cvtY,0.5,0)
laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
img_lap = cv2.convertScaleAbs(laplacian)
img_canny = cv2.Canny(img_gray,100,200)
images = [img, img_sobel, img_lap, img_canny]
titles = ['anh goc','Sobel', 'Laplace', 'Canny']
for i in range(len(images)):
    plt.subplot(2,2,i+1), plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()