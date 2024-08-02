
# Arduino-Code-Miniproject

This miniproject combines a touchless doorbell made using an arduino UNO, ultrasonic sensor and buzzer with a face detection model, enhanced with a gTTS (Google Text-to-Speech) feature.

## Table of Contents
- [Overview](#overview)
- [Working](#working)
- [Hardware Components](#hardware-components)
- [Software Requirements](#software-requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Files](#files)

## Overview
This project integrates hardware and software to create an advanced touchless doorbell system. When motion is detected, the system triggers a face recognition process and uses text-to-speech to inform the resident about the visitor.

## Working
1. The buzzer is activated, and the LED is turned on when the ultrasonic sensor detects motion.
2. The face recognition code is activated after the doorbell has been triggered.
3. The face recognition model locates the face.
4. The model classifies the face and prints the output on the terminal.
5. The gTTS model translates the face name into speech, indicating the resident of the house about the person at their doorstep.
6. The setup is shut down when the resident closes the program.

## Hardware Components
- Arduino Uno
- Buzzer
- Connecting Wires
- Resistors
- Breadboard
- USB Connector
- LED
- Ultrasonic Sensor

## Software Requirements
- Python
- gTTS
- Arduino IDE
- pygame
- OpenCV
- pickle
- serial

## Setup and Installation
1. **Arduino Setup:**
   - Connect the ultrasonic sensor, buzzer, LED, and other components to the Arduino Uno as per the circuit diagram.
   - Upload the provided Arduino code to the Arduino Uno using the Arduino IDE.

2. **Python Environment:**
   - Install Python on your system if not already installed.
   - Create a virtual environment for the project (optional but recommended).
   - Install the required Python libraries:
     ```bash
     pip install gTTS pygame opencv-python-headless pickle serial
     ```

## Usage
1. Ensure all hardware components are properly connected and the Arduino is powered on.
2. Run the face recognition script:
   ```bash
   python face_recognition.py
   ```
3. The system will start detecting motion and trigger the face recognition process upon detecting a visitor.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## files
The code is divided into multiple files which are explained below:
arduino_code.ino     - This files the basic code for the touchless doorbell which is made using the Arduino UNO, Ultrasonic Sensor and Buzzer
arduino_interface.py - This is a python file that integrates the code in embedded C and Python connecting the Arduino UNO Board with Face Detection Code
face_detection.py    - This file in python contains the python code to identify and box the face using LPBH 
face_recogniser.py   - The code in this file is responsilbe for recognising the identified face using the haarcascade classifier and also the gTTS module.
face_trainer.py      - This file is responsible for training the database used by the haarcascade classifier.
video_to_frame.py    - The code in this file is responsible for converting the input video to frames

