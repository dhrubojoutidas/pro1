
/*LinkedList.c - contains linked list fucnitonality --  C file is here */
#include "LinkedList.h"
#include <stdlib.h>
#include <stdio.h>  //for LinkedList.h no need off it 
#include "string.h"



/*  Define player directions */
#define NORTH 'n'
#define SOUTH 's'
#define EAST 'e'
#define WEST 'w'





/* Linked List functions */


void LinkedList_begin(LinkedList* list)  /*  linked list Initialize*/
{
    list->Head = NULL;
    list->Tail = NULL;
    list->size = 0;
}


void LL_InsertLast(LinkedList* list, void* data)  /* insert new node at end of linked  LIST*/
{
    Node* NewNode = (Node*)malloc(sizeof(Node));
    NewNode->data = data;
    NewNode->next = NULL;

    if (list->Tail)
    {
        list->Tail->next = NewNode;
    } else {
        list->Head = NewNode;
    }
    list->Tail = NewNode;
    list->size++;
}


void LL_Free(LinkedList* list)  /* Freeing linked list*/
{
    Node* current = list->Head;
    Node* next;
    while (current) 
    {
        next = current->next;
        free(current->data);
        free(current);
        current = next;
    }
    list->Head = NULL;
    list->Tail = NULL;
    list->size = 0;
}


void* ArrayCopy2D(void* array, int rows, int cols) /*  this fucntion is for copy of 2D array*/
{
    int (*primary)[cols] = array;
    int (*copy2D)[cols] = malloc(rows * cols * sizeof(int));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            copy2D[i][j] = primary[i][j];
        }
    }
    return copy2D;
}


void MapBoardSave(GamePhrasePTR Phrase, LinkedList* mapList) /*Functions  for Saving  present map state in linked List*/
{
    int* gamePhrase = (int*)Phrase;
    int MapRow = gamePhrase[0];
    int MapCol = gamePhrase[1];
    int (*CopyMap)[MapCol] = ArrayCopy2D((void*)gamePhrase, MapRow, MapCol);
    LL_InsertLast(mapList, (void*)CopyMap);
}



void MapFileSave(GamePhrasePTR Phrase, FILE* file, const char* action) /*Functions for Saving present map state to file log.txt*/
{
    int* gamePhrase = (int*)Phrase;
    int MapRow = gamePhrase[0];
    int MapCol = gamePhrase[1];
    int RowPlayer = gamePhrase[2];
    int ColPlayer = gamePhrase[3];
    char PD = gamePhrase[4];
    int EnemyRowSize = gamePhrase[5];
    int EnemyColSize = gamePhrase[6];
    char ED = gamePhrase[7];
    int mirrorCount = gamePhrase[12];
    int mirrorIndex = 13;

    fprintf(file, "Action: %s\n", action);
    fprintf(file, "Player: (%d, %d), Direction: %c\n", RowPlayer, ColPlayer, PD);
    fprintf(file, "Enemy: (%d, %d), Direction: %c\n", EnemyRowSize, EnemyColSize, ED);

   
    for (int i = 0; i < MapCol + 2; i++)  /* print TOP border*/ 
    {
        fprintf(file, "*");
    }
    fprintf(file, "\n");

   
    for (int i = 0; i < MapRow; i++)  /* Print map*/
    {
        fprintf(file, "*"); /*Left map border  */
        for (int j = 0; j < MapCol; j++) {
            char sign = ' '; /* Default sign is an empty space */

            for (int m = 0; m < mirrorCount; m++) 
            {
                int mirrorrow = gamePhrase[mirrorIndex + m * 3];
                int mirrorcol = gamePhrase[mirrorIndex + m * 3 + 1];
                int mt = gamePhrase[mirrorIndex + m * 3 + 2];
                if (i == mirrorrow && j == mirrorcol) {
                    sign = (mt == 0) ? '/' : '\\';
                    break;
                }
            }

            /*  Set sign for enemy */
            if (i == EnemyRowSize && j == EnemyColSize)
            {      if (ED == NORTH) {
                        sign = '^';
                   } else if (ED == SOUTH) {
                        sign = 'v';
                   } else if (ED == EAST) {
                        sign = '>';
                   } else if (ED == WEST) {
                        sign = '<';
                   }
                
            }

            /* Set sign for player */
            else if (i == RowPlayer && j == ColPlayer) {
                if (PD == NORTH) {
                    sign = '^';
                } else if (PD == SOUTH) {
                    sign = 'v';
                } else if (PD == EAST) {
                    sign = '>';
                } else if (PD == WEST) {
                    sign = '<';
                }
            }
            fprintf(file, "%c", sign);
        }
        fprintf(file, "*\n"); /* Right map border */
    }

   
    for (int i = 0; i < MapCol + 2; i++)  /*  Print bottom border*/
    {
        fprintf(file, "*");
    }
    fprintf(file, "\n\n");
}
