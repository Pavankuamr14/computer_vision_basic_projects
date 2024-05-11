import cv2
import mediapipe as mp
import time
import math

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
pTime = 0
prev_hip_x = None
prev_hip_y = None

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            # Get landmark coordinates
            cx, cy = int(lm.x * w), int(lm.y * h)

            # Check if the landmark is a hip (or any other relevant landmark)
            if id == 11:  # Adjust index based on the specific landmark you want to track
                if prev_hip_x is not None and prev_hip_y is not None:
                    # Calculate displacement between frames
                    displacement = math.sqrt((cx - prev_hip_x) ** 2 + (cy - prev_hip_y) ** 2)
                    # Calculate time elapsed between frames
                    cTime = time.time()
                    time_elapsed = cTime - pTime
                    # Calculate speed (assuming pixels per second)
                    speed = displacement / time_elapsed
                    print("Speed:", speed, "pixels/second")

                # Store current hip position for the next iteration
                prev_hip_x, prev_hip_y = cx, cy

            # Draw landmark on the image
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    # Update frame time
    pTime = time.time()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
