import cv2
import mediapipe as mp
import math



cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


class SnakeGameClass:
    def __init__(self):
        self.points = []  # all points of the snake
        self.lengths = []  # distance between each point
        self.currentLength = 0  # total length of the snake
        self.allowedLength = 150  # total allowed Length
        self.previousHead = (0, 0)  # previous head point
        self.indexFingerExtended = False  # flag to track index finger state
        self.indexFingerFound = False  # flag to track if the index finger is found

    def update(self, imgMain, hand_landmarks):
        if hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            cx, cy = int(index_finger_tip.x * imgMain.shape[1]), int(index_finger_tip.y * imgMain.shape[0])

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
    game = SnakeGameClass()
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Convert the BGR image to RGB for MediaPipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image and get hand landmarks
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]  # Assuming you are interested in the first detected hand
        game.indexFingerExtended = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < \
                                   hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
        game.indexFingerFound = True

        img = game.update(img, hand_landmarks)

        # Print the coordinates of the index finger tip
        print("Index Finger Tip Coordinates:", hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
              hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)

        # Calculate the angle between the index finger tip and the wrist
        angle = math.degrees(math.atan2(
            hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y - hand_landmarks.landmark[
                mp_hands.HandLandmark.WRIST].y,
            hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x - hand_landmarks.landmark[
                mp_hands.HandLandmark.WRIST].x))
        print("Angle between Index Finger Tip and Wrist:", angle)

    else:
        game.indexFingerFound = False

    cv2.imshow("Image", img)
    cv2.waitKey(1)
