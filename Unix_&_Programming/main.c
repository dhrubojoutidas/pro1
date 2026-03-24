#include "LinkedList.h"
#include "mirror.h"
#include "game.h"
#include "EnemyLaser.h"
#include "condition.h"
#include "ucpSleep.h"
#include "instruction.h"
#include "screenclear.h"
#include "printmap.h"
#include "DisplayBoard.h"
#include "PlayerMove.h"
#include "UpdateGame.h" 
#include "UserInput.h" 

#include <stdbool.h>
#include <stdio.h>

#include <string.h>
#include <stdlib.h>
#include <time.h>


#include <math.h>
#include <ctype.h>




/*  Define constants for laser characters */
#define LASER_HORIZONTAL '-'
#define LASER_VERTICAL '|'
#define LASER_COLOR "\033[1;31m" // Red color for laser
#define RESET_COLOR "\033[0m"    // Reset color after printing laser

/* Define constants for game parameters */
#define MIN_SIZE 5
#define MAX_SIZE 25
#define MAX_MIRRORS 100

/*  Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'





int main (int argc, char *argv[]) {

    if (argc != 2) {
        printf("Usage: %s <map.txt>\n", argv[0]);
        return 1;
    }
   
    if (strcmp(argv[0], "./laserTank") != 0) {
        printf("Please ensure the executable is named 'laserTank'.\n");
        return 1;
    }
    
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file.. <data.txt >");
        return 1;
    }

    FILE *logFile = fopen("log.txt", "w");
    if (!logFile) {
        perror("Error opening log file.");
        fclose(file);
        return 1;
    }

    int MapRow, MapCol, RowPlayer, ColPlayer, EnemyRowSize, EnemyColSize, MRow, MCol;
    char PD, ED, type;

    if (fscanf(file, "%d %d\n%d %d %c\n%d %d %c\n", &MapRow, &MapCol, &RowPlayer, &ColPlayer, &PD, &EnemyRowSize, &EnemyColSize, &ED) != 8) {
        printf("Failed to read game configuration.\n");
        fclose(file);
        fclose(logFile);
        return 1;
    }
 


    int Mirrors[MAX_MIRRORS][3]; /*  Array to store Mirrors [MRow, MCol, type (0 for '/', 1 for '\')] */
    int mirrorCount = 0;

    /*  Read Mirrors data */
    while (fscanf(file, "%d %d %c", &MRow, &MCol, &type) == 3) {
        /*if (MRow < MIN_SIZE || MRow > MAX_SIZE|| MCol < MIN_SIZE || MCol > MAX_SIZE) */
        if (MRow < 0 || MRow >= MapRow || MCol < 0 || MCol >= MapCol){
            fprintf(stderr, "\nMirror position out of bounds: (%d, %d)\n", MRow, MCol);
            return 1;  
        }

        if (type != 'f' && type != 'b') {
            fprintf(stderr, "Invalid mirror type: %c\n", type);
            return 1; 
        }
        /*  Check if mirror is in the line of  the enemy */
        if ((ED == 'e' && MRow == EnemyRowSize) ||  /* East direction, same MRow */
            (ED == 'w' && MRow == EnemyRowSize) ||  /* West direction, same MRow */
            (ED == 'n' && MCol == EnemyColSize) ||  /* North direction, same column */
            (ED == 's' && MCol == EnemyColSize)) {  /*South direction, same column */
            fprintf(stderr, "Mirror cannot be placed in enemy's line of sight at (%d, %d)\n", MRow, MCol);
            return 1; 
        }

        Mirrors[mirrorCount][0] = MRow;
        Mirrors[mirrorCount][1] = MCol;
        Mirrors[mirrorCount][2] = (type == 'f') ? 0 : 1;  /*  'f' for '/', 'b' for '\'   */        mirrorCount++;
 

        if (mirrorCount >= MAX_MIRRORS) {
            fprintf(stderr, "Maximum number of Mirrors (%d) reached.\n", mirrorCount);
            return 1 ;  
        }
    }
    fclose(file);
    if (mirrorCount == 0) 
    {
        fprintf(stderr, "Error: No Mirrors provided in the configuration file. At least one mirror is required.\n");
        return 1;  
    }

    printf("\nRead configuration: MapRow=%d, MapCol=%d, RowPlayer=%d, ColPlayer=%d, PD=%c, EnemyRowSize=%d, EnemyColSize=%d, ED=%c, MRow =%d, MCol=%d, type=%c\n",
           MapRow, MapCol, RowPlayer, ColPlayer, PD, EnemyRowSize, EnemyColSize, ED, MRow, MCol, type);

    /* Checking if the map size is in the range*/ 
    if (MapRow < MIN_SIZE || MapRow > MAX_SIZE || MapCol < MIN_SIZE || MapCol > MAX_SIZE) {
        printf("\nError: Map size (%d x %d) must be between %d and %d.\n", MapRow, MapCol, MIN_SIZE, MAX_SIZE);
        return 1;
    }

   /* Checking if the  Player coordinates  is in the range */ 
    if (RowPlayer < 0 || RowPlayer >= MapRow || ColPlayer < 0 || ColPlayer >= MapCol)  {
        printf("\nError: Player coordinates (%d, %d) must be in between %d and %d  .\n", RowPlayer, ColPlayer, MapRow,MapCol);
        return 1;
    }
    
   /* Checking if the  Enemy  coordinates  is in the range */
  /*if ((EnemyRowSize < 0 || EnemyRowSize >= MapRow || EnemyColSize < 0 || EnemyColSize >= MapCol) || (EnemyRowSize < MIN_SIZE || EnemyRowSize > MAX_SIZE || EnemyColSize < MIN_SIZE || EnemyColSize > MAX_SIZE)) */
    if (EnemyRowSize < 0 || EnemyRowSize >= MapRow || EnemyColSize < 0 || EnemyColSize >= MapCol) {
        printf("\nError: Enemy coordinates (%d, %d) must be in between %d and %d  .\n", EnemyRowSize, EnemyColSize,MapRow,MapCol);
        return 1;
    }

    PD = tolower(PD);
    ED = tolower(ED);

     
   /* Checking if the  Player Direction   is correct */ 
    if (PD != NORTH && PD != SOUTH && PD != EAST && PD != WEST) {
        printf("Error: Invalid PLAYER direction '%c'. Please use 'n', 's', 'e', or 'w'.\n", PD);
        return 1;
    }
     /* Checking if the  enemy  Direction   is correct */ 
    if (ED != NORTH && ED != SOUTH && ED != EAST && ED != WEST) {
        printf("Error: Invalid enemy direction '%c'. Please use 'n', 's', 'e', or 'w'.\n", ED);
        return 1;
    }

    /* Initialize game Phrase and map */
    GamePhrasePTR game_phrase;
    Game_initialize(&game_phrase, MapRow, MapCol, RowPlayer, ColPlayer, PD, EnemyRowSize, EnemyColSize, ED, Mirrors, mirrorCount);
    BoardDisplaying(game_phrase, '\0' ,1);
    InstructPrint();


    LinkedList mapList;   /* Initialize the linked list for map states  */ 
    LinkedList_begin(&mapList);

   
    MapBoardSave(game_phrase, &mapList); /*  Saving  initial map state */
    MapFileSave(game_phrase, logFile, "Initial Phrase");

    
    char LaserChar = '\0'; 
    int game_continue = 1;
    while (game_continue) {
        ScreenClear();
        BoardDisplaying(game_phrase, LaserChar, game_continue);
        UserInput(game_phrase, &game_continue, &mapList, logFile);
        GameStateUpdate(game_phrase, &mapList, logFile);
        
        if (WinCondition(game_phrase)) {
          
           
            BoardDisplaying(game_phrase, LaserChar,0);
            printf("\nCONGRATS-----PLAYER win!!!!!\n");
            MapFileSave(game_phrase, logFile, "!!!!!----Player Wins----!!!!!");
            game_continue = 0;
           
        }
        if (LoseCondition(game_phrase)) {
            
         
            LaserAnimationEnemy(game_phrase);
            BoardDisplaying(game_phrase, LaserChar,0);
            printf("\n -----SAD!!!!------Enemy WIN!!!!\n");
            MapFileSave(game_phrase, logFile, "\n!!!!  SAD!!-----Enemy Wins.........!!!!\n");
            game_continue =0;
           
        }
    }

    LL_Free(&mapList);
    free(game_phrase);
    fclose(logFile);
    return 0;
}

