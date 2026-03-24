
/*PlayerMove.h - contains  header file  PlayerMove.c--   */

#ifndef PLAYERMOVE_H
#define PLAYERMOVE_H
#include "LinkedList.h"
#include <string.h>

typedef void* GamePhrasePTR;     
void PlayerMove(GamePhrasePTR Phrase, char direction, LinkedList* mapList, FILE* logFile) ;
#endif