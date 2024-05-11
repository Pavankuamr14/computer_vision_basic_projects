# import cv2
# import numpy as np
#
#
# counter=0
# circle=np.zeros((4,2),np.int8)
# def MouseClicks(events, x, y, flags, params):
#     global counter
#     if events == cv2.EVENT_LBUTTONDOWN:
#         circle[counter]=x,y
#         counter=counter+1
#         # print(x, y)
#         print(circle)
# img=cv2.imread('cards.jpg')
# cv2.namedWindow("cards.jpg")
# while True:
#     if counter==4:
#         width,heigth=250,350
#         click_pts=np.float32([circle[0],circle[1],circle[2],circle[3]])
#         frame_pts=np.float32([[0,0],[width,0],[0,heigth],[width,heigth]])
#         matrix=cv2.getPerspectiveTransform(click_pts,frame_pts)
#         o_p=cv2.warpPerspective(img,matrix,(width,heigth))
#         print("heee")
#         cv2.imshow("o_p",o_p)
#     for x in range(0,4):
#         cv2.circle(img,(circle[x][0],circle[x][1]),3,(0,225,0),cv2.FILLED)
#     cv2.imshow("cards.jpg",img)
#     cv2.setMouseCallback("cards.jpg",MouseClicks)
#     cv2.waitKey(1)

#
# cv2.imshow("cards.jpg",img)
# cv2.setMouseCallback("cards.jpg", MouseClicks)
# cv2.waitKey(0)

import cv2
import numpy as np

counter = 0
circle = np.zeros((4, 2), np.int32)

def MouseClicks(events, x, y, flags, params):
    global counter
    if events == cv2.EVENT_LBUTTONDOWN:
        circle[counter] = x, y
        counter += 1
        print(circle)

img = cv2.imread('cards.jpg')
cv2.namedWindow("cards.jpg")

while True:
    if counter == 4:
        width, height = 250, 350
        click_pts = np.float32([circle[0], circle[1], circle[2], circle[3]])
        frame_pts = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(click_pts, frame_pts)
        o_p = cv2.warpPerspective(img, matrix, (width, height))
        print("heee")
        cv2.imshow("o_p", o_p)

    for x in range(0, 4):
        cv2.circle(img, (circle[x][0], circle[x][1]), 3, (0, 225, 0), cv2.FILLED)

    cv2.imshow("cards.jpg", img)
    cv2.setMouseCallback("cards.jpg", MouseClicks)
    cv2.waitKey(1)
