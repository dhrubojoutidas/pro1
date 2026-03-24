/* EnemyLaser.c -----this file conatisn the  infromation of  laser  firing  of ENEMY*/
#include <stdio.h>
//#include "EnemyLaser.h"
#include "ucpSleep.h"
#include "condition.h"


/*  Define constants for laser characters */

#define LASER_COLOR "\033[1;31m" // Red color for laser
#define RESET_COLOR "\033[0m"    // Reset color after printing laser
#define LASER_HORIZONTAL '-'
#define LASER_VERTICAL '|'

/*  Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'


void LaserAnimationEnemy(GamePhrasePTR Phrase) {
    int* gamePhrase = (int*)Phrase;
    int EnemyRowSize = gamePhrase[5]; /*  Enemy's Row*/ 
    int EnemyColSize = gamePhrase[6]; /*  Enemy's Column */
    int RowPlayer = gamePhrase[2];     /* Player's Row */
    int ColPlayer = gamePhrase[3];     /* Player's Column */
    char ED = gamePhrase[7];           /* Enemy's Direction  */
    int MapRow = gamePhrase[0];      /* Row Numberin Board */
    int MapCol = gamePhrase[1];    /*   COlumn  Number  in  Board */

    char LaserChar = (ED == NORTH || ED == SOUTH) ? LASER_VERTICAL : LASER_HORIZONTAL;

    if (LoseCondition(Phrase)) {
        printf("Enemy is firing!\n");

        int start, end, step;
        if (ED == EAST || ED == WEST) {
            start = EnemyColSize;  /* strts from enemy MCol*/
            end = ColPlayer; /* move to  payer MCol*/
            if (ED == EAST) {
                step = 1; /* move Right*/
            } else { /*  ED == WEST */
                step = -1; /* move LEFT*/
            }
            if ((ED == EAST && start > end) || (ED == WEST && start < end)) 
            {
                return;  /* Exit if direction is wrong, Enemy facing wrong direction   */
            }
        } else { /*  NORTH or SOUTH */
            start = EnemyRowSize;
            end = RowPlayer;
            if (ED == NORTH)
             {
                step = -1;  /* MOVE UP*/
            } else { /*  ED == SOUTH */
                step = 1; /* MOVE DOWN*/
            }
            if ((ED == NORTH && start < end) || (ED == SOUTH && start > end)) 
            {
                return; 
            }
        }

        for (int pos = start; (step > 0) ? pos <= end : pos >= end; pos += step) {
            printf("\033[%d;1H", 2); /*  Reset cursor to top of board for each frame */
            for (int i = 0; i < MapRow; i++) {
                printf("*"); /* Print left border */
                for (int j = 0; j < MapCol; j++) {
                    if ((ED == EAST || ED == WEST) && i == EnemyRowSize && j == pos) {
                        printf(LASER_COLOR "%c" RESET_COLOR, LaserChar);
                    } else if ((ED == NORTH || ED == SOUTH) && j == EnemyColSize && i == pos) {
                        printf(LASER_COLOR "%c" RESET_COLOR, LaserChar);
                    } else {
                        printf(" ");
                    }
                }
                printf("*\n"); /* Print right border */
            }
            for (int k = 0; k < MapCol + 2; k++) {
                printf("*"); /*  Print bottom border  */
            }
            printf("\n");
            ucpSleep(0.2); 
        }
    }
}



void HandleLaserAnimate(int MRow,int MCol, int MapRow, int MapCol, char LaserChar) {
    printf("\033[H");
    for (int i = 0; i < MapRow; i++) {
        printf("*");
        for (int j = 0; j < MapCol; j++) {
            if (i == MRow && j == MCol) {
                printf(LASER_COLOR "%c" RESET_COLOR, LaserChar);
            } else {
                printf(" ");
            }
        }
        printf("*\n");
    }
    for (int k = 0; k < MapCol + 2; k++) {
        printf("*");
    }
    printf("\n");

    ucpSleep(0.2);  /*  for the laseraniamtion*/
}
