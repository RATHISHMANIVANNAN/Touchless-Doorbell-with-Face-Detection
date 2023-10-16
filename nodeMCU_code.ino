#include <ESP8266WiFi.h>

int trigger_pin = D1;    // Connect the TRIG pin of the ultrasonic sensor to NodeMCU D1 (GPIO5)
int echo_pin = D2;       // Connect the ECHO pin of the ultrasonic sensor to NodeMCU D2 (GPIO4)
int buzzer_pin = D3;     // Connect the LONG LEG of the buzzer to NodeMCU D3 (GPIO0)
int led_pin = D7;        // Connect the LONG LEG of the LED to NodeMCU D7 (GPIO13)

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

    WiFi.begin("Your_SSID", "Your_PASSWORD"); // Connect to your Wi-Fi network
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
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
    else
    {
        Serial.println("No Motion Detected");
        Serial.print("Distance= ");
        Serial.println(distance);
        digitalWrite(buzzer_pin, LOW);
        digitalWrite(led_pin, LOW);
        delay(500);
    }
}
