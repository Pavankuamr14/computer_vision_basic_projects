# import cv2
# cap=cv2.VideoCapture("demo_video.mp4")
# frameWidth=700
# frameHeight=500
# while True:
#     success,img=cap.read()
#     img=cv2.resize(img,(frameWidth,frameHeight))
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
import cv2

img=cv2.imread("Resource/bag.png")
img=cv2.resize(img,(1000, 700))
cv2.imshow("bag",img)
cv2.waitKey(700)