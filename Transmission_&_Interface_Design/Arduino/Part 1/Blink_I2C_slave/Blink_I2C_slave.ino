// Wire Slave Receiver
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Receives data as an I2C/TWI slave device
// Refer to the "Wire Master Writer" example for use with this

// Created 29 March 2006

#include <Wire.h>

int ledPin =  13;    // LED connected to digital pin 13

void setup()
{
  // initialize the digital pin as an output:
  pinMode(ledPin, OUTPUT);     

  // join i2c bus with address #4
  Wire.begin(2);                
  // register event
  Wire.onReceive(receiveEvent);
}

void loop()
{
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  digitalWrite(ledPin, Wire.read());
}
