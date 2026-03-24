/*UpdateGame.c - C file  conatains  updating gaming state based on player direction, enemy direction, leaser and so */

#include "UpdateGame.h"
//#include "LinkedList.h"
#include "EnemyLaser.h"
#include "mirror.h"
#include <stdio.h>
#include <ctype.h>
#include <string.h>


/*  Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'


/*  Define constants for laser characters */
#define LASER_HORIZONTAL '-'
#define LASER_VERTICAL '|'

/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;

void GameStateUpdate(GamePhrasePTR Phrase, LinkedList* mapList, FILE* logFile){
    int* gamePhrase = (int*)Phrase;
    int MapRow = gamePhrase[0];
    int MapCol = gamePhrase[1];
    int RowPlayer = gamePhrase[2];
    int ColPlayer = gamePhrase[3];
    int EnemyRowSize = gamePhrase[5];
    int EnemyColSize = gamePhrase[6];
    int* laser_fire = &(gamePhrase[8]);
    int mirrorCount = gamePhrase[12]; /* mirorr number*/
    int mirrorIndex = 13;

    if (*laser_fire)  /* if the laser_fire is true, move the laser from player Position*/
    { 
        int laserRow = RowPlayer;
        int laserCol = ColPlayer;
        char direction = gamePhrase[4]; /* Player's direction */
        char laserChar = (direction == NORTH || direction == SOUTH) ? LASER_VERTICAL : LASER_HORIZONTAL;

        
        while (1) /*  Move the laser one step according to player's direction*/
        {
         
            if (direction == NORTH) {
                laserRow--;
            } else if (direction == SOUTH) {
                laserRow++;
            } else if (direction == EAST) {
                laserCol++;
            } else if (direction == WEST) {
                laserCol--;
            }

            /* Check if the laser hits the border */
            if (laserRow < 0 || laserRow >= MapRow || laserCol < 0 || laserCol >= MapCol)
            {
                break;  /* if yes,then stop animation */
         
            }


            /* Check if the laser hits the enemy tank */
            if (laserRow == EnemyRowSize && laserCol == EnemyColSize) {
                gamePhrase[11] = 1; /* Mark the enemy tank as destroyed */
                break;   /* if yes,then stop animation */
              
            }

            /* Check if the laser hits a mirror */
            int mirrorHit = 0;
            for (int m = 0; m < mirrorCount; m++) {
                int mirrorrow = gamePhrase[mirrorIndex + m * 3];
                int mirrorcol = gamePhrase[mirrorIndex + m * 3 + 1];
                int mt = gamePhrase[mirrorIndex + m * 3 + 2];

                if (laserRow == mirrorrow && laserCol == mirrorcol) 
                {
                  
                    ReflectionMirror(&direction, mt, &laserChar); /*Reflect the laser direction based on mirror type */
                    mirrorHit = 1;
                    break;
                     
                }
            }
            if (mirrorHit) continue;

            
            HandleLaserAnimate(laserRow, laserCol, MapRow, MapCol, laserChar); /* print laserAnimation*/
        }

        *laser_fire = 0;     /* Reset the laser_fire flag */
        MapBoardSave(Phrase, mapList); /* Save map state after laser firing */
        MapFileSave(Phrase, logFile, "Laser Fired");
    }
}


