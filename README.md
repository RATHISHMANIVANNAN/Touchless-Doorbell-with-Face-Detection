# Arduino-Code-Miniproject
This miniproject connects an touchless doorbell which is created using an ultrasonic sensor and buzzer with face detection model with an additional gTTs feature.

The working is explained below:
Step 1: The buzzer is activated and the led is turned on when the ultrasonic sensor detects motion 
Step 2: The face recognition code is activated after the doorbell has been triggered
Step 3: Once the face recognition model is activated it locates the face 
Step 4: Then the model Classifies the face and prints the output on the terminal
Step 5: The gTTS model translates the face name into speech indication the resident of the house about the person in front of their doorstep
Step 6: The setup is shutdown when the resident closes the program.

Hardware Components:
Arduino Uno,
Buzzer, 
Connecting Wires,
Resistors,
Breadboard,
USB Connector,
LED,
Ultrasonic Sensor.

Software:
Python,
gTTS,
Arduino IDE,
pygame,
openCV,
pickle,
serial.

