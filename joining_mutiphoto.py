import cv2
import numpy as np
img1 = cv2.imread("sprit.jpg")

img2 = cv2.imread("sprit.jpg")
print(img1.shape)
print(img2.shape)
####SCALING THE IMAGE ####
img1 = cv2.resize(img1,(0,0),None,0.5,0.5)
img2 = cv2.resize(img2,(0,0),None,0.5,0.5)
hor = np.hstack((img1, img2))
ver = np.vstack((img1, img2))

cv2.imshow("Vertical", ver)
cv2.imshow("Horizontal", hor)
cv2.waitKey(0)