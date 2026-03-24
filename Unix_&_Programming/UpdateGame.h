
/*UpdateGame.h  - Header file which links main.c with UpdateGame.c  functionality */
#include <stdio.h>
#include "LinkedList.h"

#ifndef UG_H
#define UG_H


/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;

void GameStateUpdate(GamePhrasePTR Phrase, LinkedList* mapList, FILE* logFile);
#endif