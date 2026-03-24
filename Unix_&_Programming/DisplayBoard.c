
/*displayboard.c - conatains the DispalyBoard fcuntion--  C file fucntionality is here */
//#include "DisplayBoard.h"
#include "screenclear.h"
#include "printmap.h"
#include "instruction.h"




/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;
void BoardDisplaying(GamePhrasePTR Phrase, char LaserChar , int gameOn) 
{
   
    ScreenClear();
    MapPrint(Phrase, LaserChar); /* print map with updated PD and laser*/

   
    if (gameOn) 
    {
        InstructPrint(); /* Print  instructions if not laser_fire */
    }
}
