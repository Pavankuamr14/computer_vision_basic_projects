# import cv2
# import numpy as np
# img=np.zeros((512,512,3),np.uint8)
# print(img)
# img[:]=12,125,155
# cv2.imshow("IMAGE",img)
# cv2.waitKey(0)

################################## 1st WAY TO DRAWING THE LINE
# import cv2
# import numpy as np
# img=np.zeros((700,900,3),np.uint8)
# img[:]=0,0,0
# cv2.line(img,(0,0),(500,500),(0,255,0),5)
# cv2.imshow("image",img)
# cv2.waitKey(0)

############## HERE WE WILL NOTE MANUALLY GIVE THE VALUES AS POINTS TO THE IMAGE ###################
# import cv2
# import numpy as np
# img=np.zeros((600,600,3),np.uint8)
# # PATH,POINT 1,POINT 2,COLOR,LINE THICKNESS
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(123,13,123),5)
# cv2.imshow("DRAW_TEXT_IMAGE",img)
# cv2.waitKey(0)
# DRAWING A RECTANGLE
# import cv2
# import numpy as np
# img=np.zeros((600,600,3),np.uint8)
# # cv2.rectangle(img,(150,50),(550,100),(0,225,0),5)
# #cv2.rectangle(img,staring point(upper_vlaue,down_value),ending point(upper value,bottom_value))
# cv2.rectangle(img,(50,350),(500,100),(0,225,0),cv2.FILLED)
# cv2.imshow("rectange",img)
# cv2.waitKey(0)
#DRAWING THE CRICLE
# import cv2
# import numpy as np
# img = np.zeros((650, 650, 3), np.uint8)
# cv2.circle(img,(300,300),80,(0,225,22),cv2.FILLED)
# cv2.imshow("circle",img)
# cv2.waitKey(0)

# TEXT ON THE IMAGE ##
import cv2
import numpy as np
img=np.zeros((700,700,3),np.uint8)
###########front scale=3 (size of the text)###########
cv2.putText(img,"HELLO",(200,320),cv2.FONT_HERSHEY_TRIPLEX,3,(0,222,2),2)
cv2.imshow("TEXT",img)
cv2.waitKey(0)