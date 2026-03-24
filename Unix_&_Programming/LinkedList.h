/*LinkedList.h - contains  the header file of LinkedList.c */

#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <stdio.h>
#include <string.h>



typedef struct Node {   /* Define a node structure for the linked list */
    void* data;
    struct Node* next;
} Node;



typedef struct LinkedList   /*   Define a linked list structure   */
{
    Node* Head;
    Node* Tail;
    int size;
} LinkedList;


typedef void* GamePhrasePTR;

void LinkedList_begin(LinkedList* list);

void LL_InsertLast(LinkedList* list, void* data);

void LL_Free(LinkedList* list);

void MapBoardSave(GamePhrasePTR Phrase, LinkedList* mapList);

void* ArrayCopy2D(void* array, int rows, int cols);

void MapFileSave(GamePhrasePTR Phrase, FILE* file, const char* action);
#endif



