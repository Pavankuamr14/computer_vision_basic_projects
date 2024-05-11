import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract hand structure points
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                # Check if the points are within a reasonable range
                if 0 < cx < w and 0 < cy < h:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
