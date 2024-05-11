import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Detections
        # print(results.multi_hand_world_landmarks)
        # print(results.multi_hand_landmarks)

        # Extracting 8th index values from the landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # if len(hand_landmarks.landmark) > 8:
                landmark_8 = hand_landmarks.landmark[8]
                print("Landmark 8:", landmark_8)

        # Rendering results
        # mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
        #                           mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
        #                           mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
        #                           )

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
