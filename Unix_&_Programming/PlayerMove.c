/*playermove.c - C file  conatains the playerMove fcuntionionality in here */

#include "PlayerMove.h"
#include "LinkedList.h"
#include "mirror.h"
#include <ctype.h>


/*  Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'



typedef void* GamePhrasePTR;    /*  Define GamePhrasePTR type */   
/* GamePhasePTR to an integer pointer (int*) to access the game Phase array.*/   
void PlayerMove(GamePhrasePTR Phrase, char direction, LinkedList* mapList, FILE* logFile){
    int* gamePhrase = (int*)Phrase;
    int RowPlayer = gamePhrase[2];
    int ColPlayer = gamePhrase[3];
    int EnemyRowSize = gamePhrase[5];
    int EnemyColSize = gamePhrase[6];

 
    char Dir = tolower(direction);     /* Convert direction to lowercase */

    
    if (Dir == 'w')   /* Check the direction and move the player accordingly  */
    {
       
        if (RowPlayer > 0)   /*  Move player up if possible */
        {
            RowPlayer--;
            gamePhrase[4] = NORTH; /* Update player direction */
        }
    } 
    else if (Dir == 's') {
      
        if (RowPlayer < gamePhrase[0] - 1)  /*  Move player down if possible */ 
        {
            RowPlayer++;
            gamePhrase[4] = SOUTH;  /* Update player direction */ 
        }
    }
    else if (Dir == 'a') {
       
        if (ColPlayer > 0) /*  Move player left if possible */
        {
            ColPlayer--;
            gamePhrase[4] = WEST; /* Update player direction */
        }
    }
    else if (Dir == 'd') {
        
        if (ColPlayer < gamePhrase[1] - 1)  /*  Move player righgt if possible */
        {
            ColPlayer++;
            gamePhrase[4] = EAST;  /* Update player direction */
        }
    }
    else
    {
     
        printf("WRONG!! Please enter one of the following: w, s, a, d, f.\n");
    }


    
    if (MirrorLocation(Phrase, RowPlayer, ColPlayer)) /*  Check if a move was blocked by a mirror or enemy */
    {
        printf(" SORRY!!!Movement blocked by a mirror at (%d, %d).\n", RowPlayer, ColPlayer);
        return;
    }

    printf("Moved to (%d, %d), direction %c\n", RowPlayer, ColPlayer, gamePhrase[4]); 

    /* Checking   if the player is overlapping enemy tank  and  is in the  map Range*/
    if (RowPlayer >= 0 && RowPlayer < gamePhrase[0] && ColPlayer >= 0 && ColPlayer < gamePhrase[1] && !(RowPlayer == EnemyRowSize && ColPlayer == EnemyColSize)) 
    {
       
        gamePhrase[2] = RowPlayer; /* Update player's position and direction */
        gamePhrase[3] = ColPlayer;
        MapBoardSave(Phrase, mapList); /*  Save map state in the log.txt after player move*/ 
        MapFileSave(Phrase, logFile, "Player Moved");
    } else {
        
        if (RowPlayer == EnemyRowSize && ColPlayer == EnemyColSize)
        {
            printf("ALAS!!!Movement blocked: Enemy tank  facing at (%d, %d).\n", EnemyRowSize, EnemyColSize);
        } else {
            printf("Movement out of bounds or invalid.\n");
        }
    }
}

