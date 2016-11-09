import pygame, sys, classes, random


def game_over(gameDisplay,gameOver,gameExit,gameRestart):
	while gameOver == True:
		gameDisplay.fill(classes.white)
		classes.message_to_screen(gameDisplay,"Game over",
								  classes.red,
							y_displace=-50, 
							size="large")
		classes.message_to_screen(gameDisplay,"C : recommencer, Q : quitter",
								  classes.black,
							y_displace=50, 
							size="medium")
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = False
				gameExit = True
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameExit = True
					gameOver = False
					
				if event.key == pygame.K_c:
					#gameLoop()
					gameRestart = True
					gameOver = False
					
					
	return gameOver, gameExit, gameRestart