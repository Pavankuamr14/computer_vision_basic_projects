import mediapipe as mp
import cv2
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

# Variables for speed calculation
prev_landmark_8 = None
prev_time = time.time()

current_time_millis = int(round(time.time() * 1000))

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

        # Calculate speed
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmark_8 = hand_landmarks.landmark[8]
                if prev_landmark_8 is not None:
                    # Calculate displacement
                    displacement = ((landmark_8.x - prev_landmark_8.x) ** 2 +
                                    (landmark_8.y - prev_landmark_8.y) ** 2) ** 0.5

                    prev_time = time.time()
                    time_difference = (current_time_millis - prev_time) * 1000

                    # Calculate speed
                    speed = displacement / time_difference

                    # Print or use the speed value as needed
                    print("Speed:", speed)

                # Update previous values for the next iteration
                prev_landmark_8 = landmark_8
                prev_time = time.time()

                # Rendering results (inside the loop)
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
