// Serial to I2C Master
// by Nimsiri Abhayasinghe

// This is the code of the master module that receives data from
// Serial interface and transmit it to slave module through I2C

// Created May 2013


#include <Wire.h>

void setup()
{
  Wire.begin(); // join i2c bus as master
  Serial.begin(9600); // Initialize serial interface with baud rate 9600
}



void loop()
{
  if (Serial.available() > 0){
    char c=Serial.read(); //read a character from serial interface
    Wire.beginTransmission(4); // transmit to device #4
    Wire.write(c); // sends received byte through I2C
    Serial.print(c); // re-transmit received character to serial
    Wire.endTransmission(); // end I2C transmission
  }
  
  
  // delay(500);
}
