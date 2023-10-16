import cv2
import pickle

def detect_face():
    video = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    recognizer = cv2.face_LBPHFaceRecognizer.create()
    recognizer.read("trainner.yml")

    labels = {}
    with open("labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}

    while True:
        check, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        for x, y, w, h in faces:
            face_roi = gray[y:y + h, x:x + w]

            ID, conf = recognizer.predict(face_roi)

            if conf >= 115 and conf <= 205:
                label = labels.get(ID, "Anonymous")
            else:
                label = "Anonymous"

            cv2.putText(frame, label, (x - 10, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (18, 5, 255), 2, cv2.LINE_AA)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 4)

        cv2.imshow("Video", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


