import pygame
import time
import random
import classes
import functions
from classes import *
from functions import game_over

#Trakter game
#Author: Elisee YAPI

pygame.init()

# define colors RGB values
# white = (255,255,255)
# black = (0,0,0)
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snaker')

icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)
img = pygame.image.load('tracteurHead.png')
appleimg = pygame.image.load('fruit.png')
fruit_cart = pygame.image.load('fruit_cart.png')
background = pygame.image.load("bg1.png")
#pygame.display.update()


clock = pygame.time.Clock()
FPS = 10
block_size = 20
AppleThickness = 30
gameStart = True

direction = "right"

# smallfont = pygame.font.SysFont("comicsansms", 25)
# medfont = pygame.font.SysFont("comicsansms", 50)
# largefont = pygame.font.SysFont("comicsansms", 80)

#pause
def pause():
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
					
		gameDisplay.fill(classes.white)
		classes.message_to_screen( gameDisplay,"Pause", classes.black, -100,size="large")
		classes.message_to_screen( gameDisplay,"C : continuer ou Q : quitter", classes.black, 25, display_width=display_width, display_height=display_height)
		
		pygame.display.update()
		clock.tick(5)
					
##Score

# def score(score):
	# text = smallfont.render("score: "+str(score), True, black)
	# gameDisplay.blit(text, [0,0])
	
	
#Generate Apple
def randApple_Gen():
	randApple_X = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
	randApple_Y = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0
	
	return randApple_X, randApple_Y
	
				
#Game intro
def game_intro():

	intro = True
	
	while intro:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				intro = False
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				quit()
				
		gameDisplay.fill(classes.white)
		message_to_screen( gameDisplay,"Bienvenue a Trakter",
                                  classes.green,
                                  -100,
                                  "large", display_width, display_height)
		message_to_screen( gameDisplay,"L'objectif du jeu est de ramasser les tomates",
                                  classes.black,
                                  -30,"small", display_width, display_height)
		message_to_screen( gameDisplay,"Plus vous en ramassez, plus le tracteur s'allonge",
                                  classes.black,
                                  10,"small", display_width, display_height)
		message_to_screen( gameDisplay,"si vous rentrez dans le mur ou vous meme,vous perdez",
                                  classes.black,
                                  50,"small", display_width, display_height)
		message_to_screen( gameDisplay,"C : jouer; Q : quitter; P : pause",
                                  classes.black,
                                  180,"small", display_width, display_height)
		#intro = False
		pygame.display.update()
		clock.tick(5)
		
#def snake(lead_x,lead_y,block_size):
def snake(block_size, snakeList):
	if direction == "right":
		head = pygame.transform.rotate(img,270)
	elif direction == "left":
		head = pygame.transform.rotate(img,90)
	elif direction == "up":
		head = img
	elif direction == "down":
		head = pygame.transform.rotate(img,180)
		
	gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1]))
	
	for XnY in snakeList[:-1]:
		#pygame.draw.rect(gameDisplay, classes.green, [XnY[0],XnY[1],block_size,block_size]) #fruit cart
		gameDisplay.blit(fruit_cart, ([XnY[0],XnY[1]]))

# def text_objects(text,color,size):
	# if size == "small":
		# textSurface = smallfont.render(text, True, color)
	# elif size == "medium":
		# textSurface = medfont.render(text, True, color)
	# elif size == "large":
		# textSurface = largefont.render(text, True, color)
	
	# return textSurface, textSurface.get_rect()
	
# def message_to_screen(msg,color, y_displace=0,size="small"):
	# textSurf, textRect = text_objects(msg,color,size)
	# #screen_text = font.render(msg, True, color)
	# #gameDisplay.blit(screen_text, [display_width/2, display_height/2])
	# textRect.center = (display_width/2), (display_height/2)+y_displace
	# gameDisplay.blit(textSurf, textRect)
		
def gameLoop():
    gameOver = False
    while not gameOver:
	#while not gameOver:
		global direction
		direction = "right"
		gameExit = False
		#gameOver = False
		gameRestart = False
		
		
		lead_x = display_width/2
		lead_y = display_height/2
		
		lead_x_change = 0
		lead_y_change = 0
		
		snakeList = []
		snakeLength = 1
		
		# randApple_X = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
		# randApple_Y = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0
		randApple_X, randApple_Y = randApple_Gen()
		
		while not gameExit:
		
			if gameOver:
				gameOver, gameExit, gameRestart = functions.game_over(gameDisplay,gameOver,gameExit,gameRestart)
				break
			# while gameOver == True:
				# gameDisplay.fill(white)
				# message_to_screen("Game over",
									# red, 
									# y_displace=-50, 
									# size="large")
				# message_to_screen("C pour recommencer, Q pour quitter",
									# black, 
									# y_displace=50, 
									# size="medium")
				# pygame.display.update()
								
				# for event in pygame.event.get():
					# if event.type == pygame.QUIT:
						# gameOver = False
						# gameExit = True
						
					# if event.type == pygame.KEYDOWN:
						# if event.key == pygame.K_q:
							# gameExit = True
							# gameOver = False
							
						# if event.key == pygame.K_c:
							# gameLoop()
						
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						direction = "left"
						lead_x_change = -block_size
						lead_y_change = 0
					elif event.key == pygame.K_RIGHT:
						direction = "right"
						lead_x_change = block_size
						lead_y_change = 0
					elif event.key == pygame.K_UP:
						direction = "up"
						lead_y_change = -block_size
						lead_x_change = 0
					elif event.key == pygame.K_DOWN:
						direction = "down"
						lead_y_change = block_size
						lead_x_change = 0
					elif event.key == pygame.K_p:
						pause()
				#if event.type == pygame.KEYUP:
				#	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT
				#		lead_x_change = 0
			
			if lead_x < 0 or lead_x >= display_width or lead_y < 0 or lead_y >= display_height:
				gameOver = True
			lead_x += lead_x_change
			lead_y += lead_y_change
			
			gameDisplay.fill(classes.white)
			#pygame.draw.rect(gameDisplay, black, [400,300,10,100])
			gameDisplay.blit(background, (0,0) )
			#gameDisplay.fill(red, rect=[400,300,20,20])
			
			gameDisplay.blit(appleimg, (randApple_X, randApple_Y))
			# pygame.draw.rect(gameDisplay, red, [randApple_X, randApple_Y, AppleThickness, AppleThickness])
			
			snakeHead = []
			snakeHead.append(lead_x)
			snakeHead.append(lead_y)
			snakeList.append(snakeHead)
			
			if len(snakeList) > snakeLength:
				del snakeList[0]
			
			for eachSegment in snakeList[:-1]:
				if eachSegment == snakeHead:
					gameOver = True
				
				
			snake(block_size, snakeList)
			
			classes.score(gameDisplay,snakeLength-1)
			
			pygame.display.update()
			#eat the apple
			# if lead_x == randApple_X and lead_y == randApple_Y:
				# randApple_X = round(random.randrange(0, display_width-block_size)/10.0)*10.0
				# randApple_Y = round(random.randrange(0, display_height-block_size)/10.0)*10.0
				# snakeLength += 1
				
			# if lead_x >= randApple_X and lead_x <= (randApple_X + AppleThickness):
				# if lead_y >= randApple_Y and lead_y <= (randApple_Y + AppleThickness):
					# randApple_X = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
					# randApple_Y = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
					# snakeLength += 1
			
			#My solution:		
			xcross = False
			ycross = False
			
			i = 0
			while i <= block_size:
				# comment this: leadX = lead_x + i
				if (xcross == False):
					if (lead_x+i) >= randApple_X and (lead_x+i) <= (randApple_X + AppleThickness):
						xcross = True
						
				if (ycross == False):
					if (lead_y+i) >= randApple_Y and (lead_y+i) <= (randApple_Y + AppleThickness):
						ycross = True
						
				if xcross and ycross:
					# randApple_X = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
					# randApple_Y = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0
					randApple_X, randApple_Y = randApple_Gen()
					snakeLength += 1
					break
					
				i += 1
			# another solution
			# if (lead_x > randApple_X and lead_x < (randApple_X + AppleThickness)) or ((lead_x+block_size) > randApple_X and (lead_x+block_size) < (randApple_X + AppleThickness)):
				# if (lead_y > randApple_Y and lead_y < (randApple_Y + AppleThickness)):
					# randApple_X = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
					# randApple_Y = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
					# snakeLength += 1
				# elif ((lead_y+block_size) > randApple_Y and (lead_y+block_size) < (randApple_Y + AppleThickness)):
					# randApple_X = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
					# randApple_Y = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
					# snakeLength += 1
						
						
			clock.tick(FPS)
		
		if gameRestart == False:
			
			message_to_screen( gameDisplay,"PERDU", classes.red, display_width=display_width, display_height=display_height)
			pygame.display.update()
			time.sleep(2)
			pygame.quit()
			quit()

if gameStart: #Si au debut du jeu.
	gameStart = False
	game_intro()
gameLoop()
