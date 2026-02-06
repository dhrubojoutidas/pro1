// Written by Nimsiri Abhayasinghe
// May 2013
// This is the code of SPI master which tranmits characters received from Serial to SPI

#include <SPI.h>

void setup (void)
{

  digitalWrite(SS, HIGH);  // ensure SS stays high for now
  SPI.begin ();            // begin SPI in master mode
  Serial.begin(9600);      // begin serial port at 9600 baud

  // Slow down the master a bit
  SPI.setClockDivider(SPI_CLOCK_DIV32);
  
}  // end of setup


void loop (void)
{
  if (Serial.available() > 0){
    char c=Serial.read();     // receive from serial
    digitalWrite(SS, LOW);    // enable Slave Select
    SPI.transfer (c);         // send the character received from serial to SPI
    Serial.print (c);         // print the input character back to serial
    digitalWrite(SS, HIGH);   // disable Slave Select
  }
  delay(100);
}  // end of loop
