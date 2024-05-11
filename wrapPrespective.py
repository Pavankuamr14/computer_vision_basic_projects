import cv2
import numpy as np
img1= cv2.imread("cards.jpg")
# creating the aspect ratio of the card
width,heigth=250,350

# img=np.zeros((600,600,3),np.uint8)
pts1=np.float32([[89,20],[230,20],[69,172],[218,170]])
img_pts2=np.float32([[250,16],[392,15],[247,168],[397,160]])
img_pts_3=np.float32([[407,12],[550,10],[409,161],[560,160]])
# print(len(pts1))
# print(len(img_pts2))
# print(len(img_pts_3))

print(pts1)
print(img_pts2)
print(img_pts_3)
pts2=np.float32([[0,0],[width,0],[0,heigth],[width,heigth]])
print(pts2)
matrix=cv2.getPerspectiveTransform(pts1,pts2)
print(matrix.dtype)

matrix2=cv2.getPerspectiveTransform(img_pts2,pts2)
print(matrix2.dtype)

matrix_3=cv2.getPerspectiveTransform(img_pts_3,pts2)

matrix_3 = matrix_3.astype(np.float64)  # or np.float64

print(matrix_3.dtype)

output=cv2.warpPerspective(img1,matrix,(width,heigth))
second_op=cv2.warpPerspective(img1,matrix2,(width,heigth))
third_im=cv2.warpPerspective(img1,matrix_3,(width,heigth))

for i in range(0,4):
    cv2.circle(img1,(int(pts1[i][0]),int(pts1[i][1])),5,(0,0,225),cv2.FILLED)
    cv2.circle(img1,(int(img_pts2[i][0]),int(img_pts2[i][1])),5,(0,225,0),cv2.FILLED)
    cv2.circle(img1,(int(img_pts_3[i][0]),int(img_pts_3[i][1])),5,(255,0,0),cv2.FILLED)


cv2.imshow("original image",img1)
cv2.imshow("wrapped image",output)
cv2.imshow("scond_wrapped_image",second_op)
cv2.imshow("3_wrapped_image",third_im)

cv2.waitKey(0)