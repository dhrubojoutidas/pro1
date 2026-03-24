 /*condition.c - C file  cwinding and lossing conditon fucntionality is here */


//#include "condition.h"


/*  Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'

/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;

int WinCondition(GamePhrasePTR Phrase) 
{
    int* gamePhrase = (int*)Phrase;
    return gamePhrase[11]; /* Check if the enemy tank is destroyed*/
}

int LoseCondition(GamePhrasePTR Phrase)
 {
    int* gamePhrase = (int*)Phrase;
    int RowPlayer = gamePhrase[2];
    int ColPlayer = gamePhrase[3];
    int EnemyRowSize = gamePhrase[5];
    int EnemyColSize = gamePhrase[6];
    char PD = gamePhrase[4];
    char ED = gamePhrase[7];
    
   /* printf("Player: (%d, %d), Direction: %c\n", RowPlayer, ColPlayer, PD); */
   /*  printf("Enemy: (%d, %d), Direction: %c\n", EnemyRowSize, EnemyColSize, ED); */
    
    if ((PD == NORTH && RowPlayer > EnemyRowSize && ColPlayer == EnemyColSize && ED == SOUTH) ||
        (PD == SOUTH && RowPlayer < EnemyRowSize && ColPlayer == EnemyColSize && ED == NORTH) ||
        (PD == EAST && ColPlayer < EnemyColSize && RowPlayer == EnemyRowSize && ED == WEST) ||
        (PD == WEST && ColPlayer > EnemyColSize && RowPlayer == EnemyRowSize && ED == EAST)) {
        return 1;
    }

    if ((RowPlayer == EnemyRowSize && ColPlayer < EnemyColSize && ED == 'w') ||
        (RowPlayer == EnemyRowSize && ColPlayer > EnemyColSize && ED == 'e') ||
        (ColPlayer == EnemyColSize && RowPlayer < EnemyRowSize && ED == 'n') ||
        (ColPlayer == EnemyColSize && RowPlayer > EnemyRowSize && ED == 's'))
        {
        return 1;
    }

    return 0;
}