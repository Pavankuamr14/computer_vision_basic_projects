import math
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=1)


class SnakeGameClass:
    def __init__(self):
        self.points = []  # all points of the snake
        self.lengths = []  # distance between each point
        self.currentLength = 0  # total length of the snake
        self.allowedLength = 150  # total allowed Length
        self.previousHead = 0, 0  # previous head point
        self.indexFingerExtended = False  # flag to track index finger state
        self.indexFingerFound = False  # flag to track if the index finger is found

    def update(self, imgMain, currentHand):
        if isinstance(currentHand, (list, tuple)):
            if len(currentHand) > 0:
                if isinstance(currentHand[0], (int, float)):
                    # Handle the case where pointIndex is a single value (integer or float)
                    cx, cy = currentHand[0], 0  # Assign 0 as y-coordinate or any default value
                    if len(currentHand) > 1:
                        cy = currentHand[1]

                    if self.indexFingerExtended and self.indexFingerFound:
                        self.points.append((cx, cy))
                        distance = math.hypot(cx - self.previousHead[0], cy - self.previousHead[1])
                        self.lengths.append(distance)
                        self.currentLength += distance
                        self.previousHead = cx, cy

                        # draw snake
                        for i, point in enumerate(self.points):
                            if i != 0:
                                cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                        cv2.circle(imgMain, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

        return imgMain


while True:
    game = SnakeGameClass()  # Move this line inside the loop to reset the game for each frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        myHand = hands[0]  # Assuming you are interested in the first detected hand
        lmList = myHand['lmList']
        pointIndex = lmList[8][0:2]  # Get the coordinates of the index finger tip
        pointWrist = lmList[0][0:2]  # Get the coordinates of the wrist
        fingers = detector.fingersUp(myHand)  # Pass the hand explicitly to fingersUp method

        game.indexFingerExtended = fingers[1] == 1  # Check if the index finger is extended
        game.indexFingerFound = True  # Set indexFingerFound to True when the index finger is detected

        img = game.update(img, pointIndex)

        # Print the coordinates of the index finger tip
        print("Index Finger Tip Coordinates:", pointIndex)

        # Calculate the angle between the index finger tip and the wrist
        angle = math.degrees(math.atan2(pointIndex[1] - pointWrist[1], pointIndex[0] - pointWrist[0]))
        print("Angle between Index Finger Tip and Wrist:", angle)

    else:
        game.indexFingerFound = False  # Set indexFingerFound to False when the index finger is not detected

    cv2.imshow("Image", img)
    cv2.waitKey(1)
