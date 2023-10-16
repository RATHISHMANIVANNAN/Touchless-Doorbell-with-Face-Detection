#include <SoftwareSerial.h>

SoftwareSerial mySerial(1,0); //Rx Tx

void setup() {
  // put your setup code here, to run once:
  mySerial.begin(9600);//GSM
  Serial.begin(9600); //Serial Monitor
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  mySerial.println("AT+CMGF=1");  //text mode on
  delay(1000);
  mySerial.println("AT+CMGS=\"+919043111924\"\r"); //sends SMS to the phone number. carriage return character '\r GSM will be ready to receive message
  delay(1000);
  mySerial.println("Person At Doorstep");
  delay(1000);
  mySerial.println((char)26); //sends the ctrl+z character(ASCII 26) which is used to indicate the end of the sms
  delay(1000);
}
