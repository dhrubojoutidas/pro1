
/*mirror.c - contains  mirror fucnitonality  --  C file is here */




#include "mirror.h"



/*  Define constants for laser characters */
#define LASER_HORIZONTAL '-'
#define LASER_VERTICAL '|'


/*  Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'

/*  Define GamePhrasePTR type */
//typedef void* GamePhrasePTR;


void ReflectionMirror(char* direction, int mirrorType, char* LaserChar) 
{

    /*  "f " mirror ("/") : left To Up, Right tp DOWN, UP to LEFT, DOWN to RIGHT
         "b"  mirror ("\") : left To DOWN, Right tp UP, UP to RIGHT, DOWN to LEFT
    */


    if (mirrorType == 0)  /*  Forward slash ('/')  */
    { 
        if (*direction == NORTH) {
            *direction = EAST;
            *LaserChar = LASER_HORIZONTAL; /* Change laser direction to horizontal */
        } else if (*direction == SOUTH) {
            *direction = WEST;
            *LaserChar = LASER_HORIZONTAL; 
        } else if (*direction == EAST) {
            *direction = NORTH;
            *LaserChar = LASER_VERTICAL; /* Change laser direction to vertical */
        } else if (*direction == WEST) {
            *direction = SOUTH;
            *LaserChar = LASER_VERTICAL; /* Change laser direction to vertical */
        }
    } else if (mirrorType == 1)  /*  Backward slash ('\') */
    { 
        if (*direction == NORTH) {
            *direction = WEST;
            *LaserChar = LASER_HORIZONTAL;  /* Change laser direction to horizontal */
            *direction = EAST;
            *LaserChar = LASER_HORIZONTAL; 
        } else if (*direction == EAST) {
            *direction = SOUTH;
            *LaserChar = LASER_VERTICAL;   /* Change laser direction to vertical */
        } else if (*direction == WEST) {
            *direction = NORTH;
            *LaserChar = LASER_VERTICAL; 
        }
    }
}


/* Fucntion to chekcing if  specific pos contains mirror*/

int MirrorLocation(GamePhrasePTR Phrase, int MRow, int MCol)
 {
    int* gamePhrase = (int*)Phrase;
    int mirrorCount = gamePhrase[12]; /* mirror num storeing in map state */
    int mirrorIndex = 13;   /* start index for mirror in the game state array */

    for (int i = 0; i < mirrorCount; i++) {
        int mirrorrow = gamePhrase[mirrorIndex + i * 3]; /*  Mirror MRow*/ 
        int mirrorcol = gamePhrase[mirrorIndex + i * 3 + 1]; /*  Mirror column */
        if (mirrorrow == MRow && mirrorcol == MCol) {
            return 1;  /* if  is located in this giveb pos*/
        }
    }
    return 0; /* if no mirror  is located */
}