CC=gcc
CFLAGS=-Wall 
OBJ=main.o  LinkedList.o mirror.o game.o EnemyLaser.o condition.o ucpSleep.o instruction.o screenclear.o printmap.o  DisplayBoard.o PlayerMove.o  UpdateGame.o UserInput.o
EXEC=laserTank

laserTank: $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)


main.o: main.c  LinkedList.h mirror.h  game.h EnemyLaser.h condition.h ucpSleep.h instruction.c screenclear.h  printmap.h  DisplayBoard.h  PlayerMove.h  UpdateGame.h UserInput.h
	$(CC) $(CFLAGS) main.c -c

LinkedList.o: LinkedList.c LinkedList.h
	$(CC) $(CFLAGS)  LinkedList.c -c
		
mirror.o: mirror.c mirror.h
	$(CC) $(CFLAGS)  mirror.c  -c

game.o : game.c game.h
	$(CC) $(CFLAGS) game.c -c	
				
EnemyLaser.o:EnemyLaser.c  EnemyLaser.h
	$(CC) $(CFLAGS)  EnemyLaser.c  -c		

condition.o	:condition.h condition.c
	$(CC) $(CFLAGS) condition.c -c	

ucpSleep.o: ucpSleep.c ucpSleep.h 
	$(CC) $(CFLAGS) ucpSleep.c -c

instruction.o : instruction.h instruction.c 
	$(CC) $(CFLAGS) instruction.c -c


screenclear.o :screenclear.h screenclear.c 
	$(CC) $(CFLAGS)  screenclear.c -c	


	
printmap.o : printmap.c printmap.h condition.h
	$(CC) $(CFLAGS) printmap.c -c

	
		
DisplayBoard.o: DisplayBoard.h DisplayBoard.c printmap.h screenclear.h instruction.h
	$(CC) $(CFLAGS)  DisplayBoard.c  -c 
	
	
PlayerMove.o : PlayerMove.h PlayerMove.c  LinkedList.h  mirror.h
	$(CC) $(CFLAGS) PlayerMove.c -c


UpdateGame.o : UpdateGame.h UpdateGame.c  LinkedList.h  mirror.h EnemyLaser.h
	$(CC) $(CFLAGS) UpdateGame.c -c
	
UserInput.o : UserInput.c UserInput.h PlayerMove.h LinkedList.h
	$(CC) $(CFLAGS) UserInput.c -c
	

	




clean:
	rm -f $(OBJ) $(EXEC)
