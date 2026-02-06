// Wire Master Writer
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Writes data to an I2C/TWI slave device
// Refer to the "Wire Slave Receiver" example for use with this

// Created 29 March 2006

#include <Wire.h>

int ledPin =  13;    // LED connected to digital pin 13

void setup()
{
  // initialize the digital pin as an output:
  pinMode(ledPin, OUTPUT);     

  // join i2c bus (address optional for master)
  Wire.begin();
}

void loop()
{
  digitalWrite(ledPin, HIGH);   // set the LED on
  Wire.beginTransmission(4);    // transmit to device #4
  Wire.write(HIGH);              // sends one byte  
  Wire.endTransmission();       // stop transmitting
  Wire.beginTransmission(2);    // transmit to device #2
  Wire.write(LOW);              // sends one byte  
  Wire.endTransmission();       // stop transmitting
  delay(1000);                  // wait for a second

  digitalWrite(ledPin, LOW);    // set the LED off
  Wire.beginTransmission(4);    // transmit to device #4
  Wire.write(LOW);               // sends one byte  
  Wire.endTransmission();       // stop transmitting
  Wire.beginTransmission(2);    // transmit to device #4
  Wire.write(HIGH);              // sends one byte  
  Wire.endTransmission();       // stop transmitting
  delay(1000);                  // wait for a second
}

