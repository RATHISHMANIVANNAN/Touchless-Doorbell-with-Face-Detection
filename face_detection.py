import cv2

# Load the pre-trained face detection classifier (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a VideoCapture object for accessing the webcam
video_capture = cv2.VideoCapture(0)

while True:
   
    ret, frame = video_capture.read()      # Read a frame from the webcam

   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # Convert the frame to grayscale for face detection

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))   # Detect faces in the grayscale frame

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle around the face

    
    cv2.imshow('Face Detection', frame)   # Display the frame with detected faces

   
    if cv2.waitKey(1) & 0xFF == ord('q'):   # Exit the loop when 'q' key is pressed
        break


video_capture.release()  # Release the VideoCapture and close all OpenCV windows
cv2.destroyAllWindows()
