/*UserInput.c - C file  conatains  user input  fcuntionionality  */

#include "UserInput.h"
#include "PlayerMove.h"
#include "LinkedList.h"
#include <ctype.h>



/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;
void UserInput(GamePhrasePTR Phrase, int* game_continue, LinkedList* mapList, FILE* logFile) {
    char input;
    printf("Enter command: ");
    scanf(" %c", &input); /* It reads the input character using scanf. */
    int* gamePhrase = (int*)Phrase;

    if (tolower(input) == 'f') {
        gamePhrase[8] = 1; /* Set  laser laser_fire flag */
        MapBoardSave(Phrase, mapList); /* Save map state after firing laser */
        MapFileSave(Phrase, logFile, "Laser Fired");
    
    } else if (tolower(input) == 'q')
     {
        printf("Unfortunately!! U  QUIT the game .\n");
        *game_continue =0; 
  
    }else if (input == 'w' || input == 's' || input == 'a' || input == 'd') {
        PlayerMove(Phrase, input, mapList, logFile); 
    } else {
       
        printf("Invalid command. Please enter one of the following: w, s, a, d, f, q.\n");
    }
}