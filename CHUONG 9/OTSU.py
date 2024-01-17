# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:14:50 2023

@author: Duy Hao
"""
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('../anh.jpg')
h,w = img.shape[:2]
left = 0
bottom = 0
top = int(input('Nhap chieu cao: '))
right = int(input('Nhap chieu rong: '))
img_drop = img[left:right, bottom:top]
img_gray = cv2.cvtColor(img_drop, cv2.COLOR_BGR2GRAY)
ret,ostu = cv2.threshold(img_gray,0,255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
images = [img, img_drop, img_gray, ostu]
titles = ['anh goc', 'anh cat', 'anh xam',' ostu']
for i in range(len(images)):
    plt.subplot(2,2,i+1), plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
cv2.waitKey(0)
cv2.destroyAllWindows()