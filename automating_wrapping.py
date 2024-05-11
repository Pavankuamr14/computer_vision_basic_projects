import cv2
import numpy as np
img=cv2.imread('cards.jpg')
points=np.float32([[[89,20],[230,20],[69,172],[218,170]],
    [[250,16],[392,15],[247,168],[397,160]],
    [[407,12],[550,10],[409,161],[560,160]],
    [[62,193],[212,186],[50,366],[213,359]],
    [[246,185],[396,176],[254,355],[410,347]],
    [[418,180],[567,174],[422,350],[583,345]],
    [[39,401],[206,389],[33,603],[210,589]],
    [[243,379],[405,378],[239,582],[411,574]],
    [[437,375],[598,368],[447,572],[622,564]]])

width,heigth=150,250
screen_points=np.float32([[0,0],[width,0],[0,heigth],[width,heigth]])
holder=[]
for i in range(len(points)):
    matrix=cv2.getPerspectiveTransform(points[i],screen_points)
    output = cv2.warpPerspective(img, matrix, (width, heigth))
    holder.append(output)
print(holder)
    #cv2.imshow("original image", img)
hor=np.hstack(holder)
cv2.imshow("original image", img)
cv2.imshow("wrapped image",hor)
cv2.waitKey(0)

# for j in range(len(holder)):
#     horizantal_image=np.hstack((hor,holder[j]))
#     # cv2.imshow("original image", img)
#     cv2.imshow("wrapped image",horizantal_image )
#     cv2.waitKey(700)



