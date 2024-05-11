import cv2
import numpy as np

# Create video capture object for the camera
cap = cv2.VideoCapture(0)

# Get the resolution of the camera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

while True:
    # Read frame from the video capture object
    ret, frame = cap.read()

    # Check if frame was successfully read
    if not ret:
        print("Error: Could not read frame from video capture.")
        break

    # Resize the frame
    frame = cv2.resize(frame, (0, 0), None, 0.5, 0.5)

    # Write the frame to the video file
    out.write(frame)

    # Display the frame
    cv2.imshow("Camera", frame)

    # Display the vertical stacked image in a separate window
    ver = np.vstack((frame, frame))
    cv2.imshow("Vertical", ver)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break

# Release the video capture object and close windows
cap.release()
out.release()
cv2.destroyAllWindows()



























