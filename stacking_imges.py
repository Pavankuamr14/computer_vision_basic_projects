import cv2
import numpy as np
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale,scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

kernel=np.ones((5,5),np.uint8)
img=cv2.imread("sprit.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blur=cv2.GaussianBlur(img,(3,3),4)
dul=cv2.dilate(img,kernel,iterations=1)
erode=cv2.erode(img,kernel,iterations=1)
canny=cv2.Canny(img,130,120)
StackImages=stackImages(2.8,([img,gray,blur],[dul,canny,erode]))
cv2.imshow("STACKED IMAGE",StackImages)
# cv2.imshow("original image",img)
# cv2.imshow("dultated image", dul)
# cv2.imshow("grey",gray)
# cv2.imshow("blur",blur)
# cv2.imshow("canny",canny)
# cv2.imshow("Erode",erode)
cv2.waitKey(0)