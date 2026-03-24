/*displayboard.h - Header file which links main.c with dispalyboard.c functionality */

#ifndef DISPLAYBOARD_H
#define DISPLAYBOARD_H

typedef void* GamePhrasePTR;/*  Define GamePhrasePTR type */
void BoardDisplaying(GamePhrasePTR Phrase, char LaserChar, int gameOn);
#endif