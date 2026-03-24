/*mirror.h - contains  header file  mirror.c--   */


#ifndef MIRROR_H
#define MIRROR_H

/*  Define GamePhrasePTR type */
typedef void* GamePhrasePTR;
int MirrorLocation(GamePhrasePTR Phrase, int MRow, int MCol);
void ReflectionMirror(char* direction, int mirrorType, char* LaserChar);
#endif