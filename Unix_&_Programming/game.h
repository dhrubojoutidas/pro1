 /*game.h - Header file which links main.c with game.c functionality */


#ifndef GAME_H
#define GAME_H

/*Define GamePhrasePTR type */ 
typedef void* GamePhrasePTR;
void Game_initialize(GamePhrasePTR* Phrase, int MapRow, int MapCol, int RowPlayer, int ColPlayer, char PD, int EnemyRowSize, int EnemyColSize, char ED, int Mirrors[][3], int mirrorCount);

#endif