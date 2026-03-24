/*UserInput.h - Header file which links main.c with UserInput.cfunctionality */

#include <stdio.h>
#include "LinkedList.h"

#ifndef USERINPUT_H
#define USERINPUT_H


/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;

void UserInput(GamePhrasePTR Phrase, int* game_continue, LinkedList* mapList, FILE* logFile);
#endif



