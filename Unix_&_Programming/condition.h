
/*conditon.h - Header file which links main.c with condition.c functionality */

#ifndef CONDITION_H
#define CONDITION_H



/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;

int WinCondition(GamePhrasePTR Phrase);
int LoseCondition(GamePhrasePTR Phrase);


#endif