import cv2
import numpy as np
 
img = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape
 
denoised = cv2.GaussianBlur(img,(5,5),0)
filter = cv2.Laplacian(denoised,cv2.CV_64F)
 
cv2.imshow('Original',img)
cv2.imshow('Laplacian Filter',filter)
 
cv2.waitKey(0)