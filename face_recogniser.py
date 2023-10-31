import cv2
import pickle
from gtts import gTTS
import pygame

def say_my_name(person):
    tts = gTTS(person+" has arrived at your doorstep", lang='en')           #creates text to speech object in english
    tts.save("labels.mp3")                                                  #saves the audio in the file label.mp3
    pygame.init()                                                           #initializes pygame library for audio playback
    pygame.mixer.music.load("labels.mp3")                                   #uploads the labels.mp3 file into pygame for audio play back
    pygame.mixer.music.play()                                               #plays the loaded audio file

def detect_face():
    flag=True
    video = cv2.VideoCapture(0)                                             #initializes video capture object 
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #loads pre trianed classifier
    recognizer = cv2.face_LBPHFaceRecognizer.create()                       #initializes LBHPF recognizer
    recognizer.read("trainner.yml")                                         #loads previously trained trainner.yml file

    labels = {}                                                             #initializing an empty set for storing labels
    with open("labels.pickle", 'rb') as f:                                  #is used to open the labels.pickle and loads the labels and populates them
        og_labels = pickle.load(f)                            
        labels = {v: k for k, v in og_labels.items()}

    while True:                                                  
        check, frame = video.read()                                                
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)     #converting image to black and white 

        for x, y, w, h in faces:                                                    
            face_roi = gray[y:y + h, x:x + w]

            ID, conf = recognizer.predict(face_roi)                          #for each face calculates ID and confidence

            if conf >= 115 and conf <= 205:                                  #confidence is used to detect the face
                label = labels.get(ID, "Anonymous")          
                if flag:
                    say_my_name(label)
                    flag=False

            else:
                label = "Anonymous"                                          #if no face is identified it displays anonymous
                if flag:
                    say_my_name(label)
                    flag=False

            cv2.putText(frame, label, (x - 10, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (18, 5, 255), 2, cv2.LINE_AA)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 4)

        cv2.imshow("Video", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
'''
if __name__ == "__main__" :
    detect_face()
'''
