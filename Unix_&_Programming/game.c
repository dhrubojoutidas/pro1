/*game.c - contains game Initializing fucnitonality  Game_initialize fucntion--  C file is here */
#include <stdio.h>
#include <stdlib.h>

/* Define constants for game parameters */
#define MAX_MIRRORS 20
/*Define GamePhrasePTR type */ 
typedef void* GamePhrasePTR;

void Game_initialize(GamePhrasePTR* Phrase, int MapRow, int MapCol, int RowPlayer, int ColPlayer, char PD, int EnemyRowSize, int EnemyColSize, char ED, int Mirrors[][3], int mirrorCount) {
    *Phrase = malloc((13 + MAX_MIRRORS * 3) * sizeof(int)); /*  Allocate memory for the game state*/ 
    int* gamePhrase = (int*)*Phrase;
    gamePhrase[0] = MapRow;
    gamePhrase[1] = MapCol;
    gamePhrase[2] = RowPlayer;
    gamePhrase[3] = ColPlayer;
    gamePhrase[4] = PD;
    gamePhrase[5] = EnemyRowSize;
    gamePhrase[6] = EnemyColSize;
    gamePhrase[7] = ED;
    gamePhrase[8] = 0;  /*  Laser fire flag initially set to 0*/ 
    gamePhrase[11] = 0;  /*   Enemy destroyed flag*/ 
    gamePhrase[12] = mirrorCount;  /*mirror count*/

   
    int mirrorIndex = 13; // Starting index for Mirrorss
    for (int i = 0; i < mirrorCount; i++)  /* Store Mirrors in game state*/
    {
        gamePhrase[mirrorIndex++] = Mirrors[i][0]; /*  Row*/
        gamePhrase[mirrorIndex++] = Mirrors[i][1]; /* Column */ 
        gamePhrase[mirrorIndex++] = Mirrors[i][2]; /*  Type (0 for '/', 1 for '\\') */
    }

     
    if (*Phrase == NULL)  /* Check if memory allocation was successful */
    {
        fprintf(stderr, "Memory allocation failed\n");

        return;
    } else {
        printf("Memory successfully allocated using malloc.\n");
    }
}