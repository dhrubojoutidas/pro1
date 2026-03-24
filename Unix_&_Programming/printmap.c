/*printmap.c - C file  conatains the  game  map printing fcuntionionality in here */

#include "stdio.h"
#include"printmap.h"
#include "condition.h"


//#include "mirror.h"


#define LASER_COLOR "\033[1;31m" // Red color for laser
#define RESET_COLOR "\033[0m"    // Reset color after printing laser

/*Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'


typedef void* GamePhrasePTR;


void MapPrint(GamePhrasePTR Phrase, char LaserChar) 
{
    int* gamePhrase = (int*)Phrase;
    int MapRow = gamePhrase[0];
    int MapCol = gamePhrase[1];
    int RowPlayer = gamePhrase[2];
    int ColPlayer = gamePhrase[3];
    int EnemyRowSize = gamePhrase[5];
    int EnemyColSize = gamePhrase[6];
    char PD = gamePhrase[4];
    char ED = gamePhrase[7];
    int mirrorCount = gamePhrase[12];
    int mirrorIndex = 13;

   
   /*  Check if player or enemy has lost*/
    int EnemyLost = WinCondition(Phrase);  /* enemy will be X when Enemylost && !player */
    int PlayerLost = LoseCondition(Phrase);

    for (int i = 0; i < MapCol + 2; i++) 
    {
        printf("*");
    }
    printf("\n");


    for (int i = 0; i < MapRow; i++)  /*  print map*/
    {
        printf("*"); /* Left map border */

        for (int j = 0; j < MapCol; j++) {
            char sign = ' '; /* Default sign is an empty space */

            for (int m = 0; m < mirrorCount; m++) 
            {
                int mirrorrow = gamePhrase[mirrorIndex + m * 3];
                int mirrorcol = gamePhrase[mirrorIndex + m * 3 + 1];
                int mt = gamePhrase[mirrorIndex + m * 3 + 2];
                if (i == mirrorrow && j == mirrorcol) 
                {
                    sign = (mt == 0) ? '/' : '\\'; /* if mt = 0 , it will sign forwardslash "/"mirror,otherwise  "\" miror*/
                  
                   m = mirrorCount;
                }
            }

          
            if (i == EnemyRowSize && j == EnemyColSize) /* Set sign for enemy*/
            {
                if (gamePhrase[11]){ 
                    sign = 'X';   /*  enemy lost */
                }
                else
                {
                     if (ED == NORTH) {
                        sign = '^';
                     } else if (ED == SOUTH) {
                        sign = 'v';
                     } else if (ED == EAST) {
                        sign = '>';
                      } else if (ED == WEST) {
                        sign = '<';
                      }
                }
            }

          
            else if (i == RowPlayer && j == ColPlayer)  /* Set sign for PLAYER*/
            {
                sign = '^'; /*  Assume facing right */
                if (PD == NORTH) {
                    sign = '^';
                } else if (PD == SOUTH) {
                    sign = 'v';
                } else if (PD == EAST) {
                    sign = '>';
                } else if (PD == WEST) {
                    sign = '<';
                }
                if (PlayerLost && !EnemyLost) /* when enemy wins && player did not win */ 
                    sign = 'X';  /*  Player lost */
            }

            /* Set sign for laser  */
            else if (LaserChar != '\0' && ((PD == EAST && i == RowPlayer && j > ColPlayer) ||
                                           (PD == WEST && i == RowPlayer && j < ColPlayer) ||
                                           (PD == SOUTH && i > RowPlayer && j == ColPlayer) ||
                                           (PD == NORTH && i < RowPlayer && j == ColPlayer))) 
           {
                
                printf(LASER_COLOR "%c" RESET_COLOR, LaserChar); /* Print laser with color*/
               
            }
            printf("%c", sign);
        }
        printf("*\n"); /* Right map border */
    }

    for (int i = 0; i < MapCol + 2; i++)  /*Print the bottom border*/
    {
        printf("*");
    }
    printf("\n");
}






