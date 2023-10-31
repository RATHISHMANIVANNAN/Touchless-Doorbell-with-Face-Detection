import cv2
import os

# Create a directory to store the captured frames
output_directory = 'captured_frames'
os.makedirs(output_directory, exist_ok=True)

# Initialize the webcam
video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera, you can change it to a different camera if needed

frame_count = 0  # Counter to track the frame number

while True:
    # Read a frame from the webcam
    ret, frame = video_capture.read()
    
    frame_count += 1
    
    if frame_count>200:
        break

    # Save the frame as an image in the output directory
    frame_filename = os.path.join(output_directory, f'frame_{frame_count}.jpg')
    cv2.imwrite(frame_filename, frame)

    # Display the live video feed
    cv2.imshow('Live Video', frame)

    # Press 'q' to exit the loop and stop capturing frames
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
video_capture.release()
cv2.destroyAllWindows()
