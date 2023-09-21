int trigger_pin = 9;    // Connect the TRIG pin of the ultrasonic sensor to Arduino pin 9
int echo_pin = 10;      // Connect the ECHO pin of the ultrasonic sensor to Arduino pin 10
int buzzer_pin = 11;    // Connect the LONG LEG of the buzzer to Arduino pin 11
int led_pin = 13;       // Connect the LONG LEG of the LED to a resistor and then to Arduino pin 13

int time;
int distance; 
int motionThreshold = 7; // Adjust this threshold as needed

void setup() 
{
    Serial.begin(9600); 
    pinMode(trigger_pin, OUTPUT); 
    pinMode(echo_pin, INPUT);
    pinMode(buzzer_pin, OUTPUT);
    pinMode(led_pin, OUTPUT);
}

void loop() 
{
    digitalWrite(trigger_pin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigger_pin, LOW);
    time = pulseIn(echo_pin, HIGH);
    distance = (time * 0.034) / 2;

    if (distance <= motionThreshold) 
    {
        Serial.println("Motion Detected");
        Serial.print("Distance= ");              
        Serial.println(distance);        
        digitalWrite(buzzer_pin, HIGH);
        digitalWrite(led_pin, HIGH);
        delay(500);
    }
    else {
        Serial.println("No Motion Detected");
        Serial.print("Distance= ");              
        Serial.println(distance);        
        digitalWrite(buzzer_pin, LOW);
        digitalWrite(led_pin, LOW);
        delay(500);        
    } 
}
