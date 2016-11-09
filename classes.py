import pygame, sys, random
pygame.init()
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


#define colors RGB values
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
	
def color(color):
	#define colors RGB values
	if color == "white":
		col = (255,255,255)
	elif color == "black":
		col = (0,0,0)
	elif color == "red":
		col = (255,0,0)
	elif color == "green":
		col = (0,255,0)
	elif color == "blue":
		col = (0,0,255)
		
	return col
	
def score(gameDisplay,score):
	text = smallfont.render("score: "+str(score), True, black)
	gameDisplay.blit(text, [0,0])
	
def text_objects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)
	
	return textSurface, textSurface.get_rect()
	

def message_to_screen(gameDisplay,msg,color, y_displace=0,size="small",display_width=800, display_height=600):
	
	textSurf, textRect = text_objects(msg,color,size)
	# screen_text = font.render(msg, True, color)
	# gameDisplay.blit(screen_text, [display_width/2, display_height/2])
	textRect.center = (display_width/2), (display_height/2)+y_displace
	gameDisplay.blit(textSurf, textRect)