/*screenclear.c - C file  conatains the  fcuntionionality of clearing the screen every user input*/

#include  "screenclear.h"
#include "stdlib.h"

void ScreenClear()
{
    /* Execute the appropriate system command to clear the screen */
    system("cls || clear"); /* cls is for windos based .. clear = Unix based sysmtem*/
}

