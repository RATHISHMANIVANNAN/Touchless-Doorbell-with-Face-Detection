import serial
import time
from face_recognise import detect_face
ArduinoSerial = serial.Serial(port='COM3', baudrate=9600)
time.sleep(2)

while True:
  detection = ArduinoSerial.readline().decode().strip()
  print(detection)
  if 'Motion Detected' in detection:
    detect_face()
 
