import cv2
import numpy as np
 
img = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape
 
sobel_horizontal = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 5)
sobel_vertical = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
 
cv2.imshow('Original',img)
cv2.imshow('Sobel Horizontal Filter',sobel_horizontal)
cv2.imshow('Sobel Vertical Filter',sobel_vertical)
 
cv2.waitKey(0)