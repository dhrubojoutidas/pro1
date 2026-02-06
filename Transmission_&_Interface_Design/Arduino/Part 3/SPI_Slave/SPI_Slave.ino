// Written by Nimsiri Abhayasinghe
// May 2013
// This is the code of the Slave that prints characters received from SPI to Serial 


#include <SPI.h>

void setup (void)
{
  Serial.begin (9600);   // debugging

  // have to send on master in, *slave out*
  // pinMode(MISO, OUTPUT);
  
  // turn on SPI in slave mode
  SPCR |= _BV(SPE);


  // now turn on interrupts
  SPI.attachInterrupt();

}  // end of setup


// SPI interrupt routine
ISR (SPI_STC_vect)
{
char c = SPDR;  // grab byte from SPI Data Register
Serial.print(c);
}  // end of interrupt routine SPI_STC_vect

// main loop - wait for flag set in interrupt routine
void loop (void)
{
  delay(100);  // Nothing to do in the main loop

}  // end of loop
