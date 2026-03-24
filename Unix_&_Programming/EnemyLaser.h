/*EnemyLaser.h ----- Header file of EnemeyLaser.c */

#ifndef ENEMYLASER_H
#define ENEMYLASER_H

/*  Define GamePhrasePTR type */

typedef void* GamePhrasePTR;
void HandleLaserAnimate(int MRow, int MCol, int MapRow, int MapCol, char LaserChar);
void LaserAnimationEnemy(GamePhrasePTR Phrase);
#endif