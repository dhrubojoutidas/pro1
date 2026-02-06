// Serial to I2C Slave
// by Nimsiri Abhayasinghe

// This is the code of the slave module that receives data from
// I2C interface sent by master module and transmit using serial
// interface

// Created May 2013


#include <Wire.h>

void setup()
{
  Wire.begin(4);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event for I2C receive
  Serial.begin(9600);           // start serial for output with baud rate 9600
}

void loop()
{
  
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  char x = Wire.read();    // receive byte from I2C as a character
  Serial.print(x);  // print the integer
  
}
