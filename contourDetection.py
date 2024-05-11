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
## creating a window for knowing the edge using kenny Edge Detector

def empty(a):
    pass


cv2.namedWindow("Parameters")

cv2.resizeWindow("Parameters",640,240)

cv2.createTrackbar('Threshold1','Parameters',150,255,empty)

cv2.createTrackbar('Threshold2','Parameters',2550,255,empty)





img=cv2.imread('sprit.jpg')

imgBlur=cv2.GaussianBlur(img,(7,7),1)

imggray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

Threshold1=cv2.getTrackbarPos("Threshold1","Parameters")

Threshold2=cv2.getTrackbarPos("Threshold2","Parameters")

print(Threshold1)

print(Threshold2)

canny_img=cv2.Canny(img,Threshold1,Threshold2)

imgStack=stackImages(0.8,([img,imggray,canny_img]))



cv2.imshow("Result",imgStack)

cv2.waitKey(0)






















# import cv2
# import numpy as np
#
# frameWidth=640
# frameHeight=480
#
# cap=cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
#
#
#
# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale,scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor = np.hstack(imgArray)
#         ver = hor
#     return ver
#
#
#
# while True:
#     success,img=cap.read()
#     imgBlur=cv2.GaussianBlur(img,(7,7),1)
#     imgGray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
#     imgStack=stackImages(0.8,([img,imgBlur,imgGray]))
#     cv2.imshow("Result",imgStack)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break