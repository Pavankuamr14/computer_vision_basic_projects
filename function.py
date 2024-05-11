# TYPE-1 to change the image color to gray
# import cv2
# img=cv2.imread('sprit.jpg',0)
# cv2.imshow("GRAY",img)
# cv2.waitKey(0)
# TYPE-2 TO CHANGE A IMG COLOR  TO ANOTHER COLOR
# import cv2
# img=cv2.imread("sprit.jpg")
# color1=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
# color2=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
# cv2.imshow("original_pic",img)
# cv2.imshow("color_pic1",color1)
# cv2.imshow("color_pic2",color2)
# cv2.waitKey(0)
# MAKING THE IMAGE INTO BLUR
# import cv2
# img=cv2.imread("sprit.jpg")
# img_blur=cv2.GaussianBlur(img,(9,9),0)
# cv2.imshow("original_image",img)
# cv2.imshow("Blur_image",img_blur)
# cv2.waitKey(0)
#MAKING THE IMAGE TO CANNY(DARWING THE OUTLINE TO THE IMAGE)
# import cv2
# img=cv2.imread("sprit.jpg")
# # cv2.Canny(image_path,threshold_value)
# # img_canny=cv2.Canny(img,50,50)
# img_canny=cv2.Canny(img,300,300)
# cv2.imshow("original_image",img)
# cv2.imshow("IMAGE_CANNY",img_canny)
# cv2.waitKey(0)
# DILATION OF THE PIC (MAKING EDGES TO CONTRACT OR THIKER) and Errosion
import cv2
import numpy as np

# kernel=np.ones((5,5),np.uint8)
# img=cv2.imread("sprit.jpg")
# img_dilation=cv2.dilate(img,kernel,iterations=1)
# img_errosion=cv2.erode(img_dilation,kernel,iterations=1)
# cv2.imshow("original_image",img)
# cv2.imshow("image_dilation",img_dilation)
# cv2.imshow("image_Errosion",img_errosion)
# cv2.waitKey(0)
##################################################################################
# image resize
# import cv2
# img=cv2.imread("sprit.jpg")
# print(img.shape)
# cv2.imshow("original pic",img)
# width=1000
# height=800
# img_resize=cv2.resize(img,(width,height))
# print(img_resize.shape)
# cv2.imshow("resize image",img_resize)
# cv2.waitKey(0)

# image crop
# import cv2
# img=cv2.imread('sprit.jpg')
# print(img.shape)
# img_cropped=img[0:109,0:120]
# cv2.imshow("Original_image",img)
# cv2.imshow("cropped_image",img_cropped)
# cv2.waitKey(0)

#RESIZING THE CROPPED IMAGE BACK TO ORIGINAL IMAGE
# import  cv2
# img=cv2.imread('sprit.jpg')
# img_cropp=img[0:109,0:120]
# img_resize=cv2.resize(img_cropp,(img.shape[1],img.shape[0]))
# cv2.imshow("original_image",img)
# cv2.imshow("cropped_image",img_cropp)
# cv2.imshow("resize_image",img_resize)
# cv2.waitKey(0)