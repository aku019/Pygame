import pygame
import time
import random
import math
from pygame import mixer
pygame.init() #initialize the pygame
screen = pygame.display.set_mode((800,600)) #create the screen
pygame.display.set_caption("Space invaders")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
mixer.music.load("background.wav")
mixer.music.play(-1)
background=pygame.image.load("background.png")
playerImg=pygame.image.load("space-invaders.png")

playerX=370
playerY=480
px_c=0
py_c=0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


score_value= 0
font = pygame.font.Font('freesansbold.ttf',32)
over_font=pygame.font.Font('freesansbold.ttf',64)
textX=10
testY=10
def game_over_text():
	score=over_font.render("GAME OVER",True,(255,255,255))
	screen.blit(score,(200,250))
def show_score(x,y):
	score=font.render("Score :"+str(score_value),True,(255,255,255))
	screen.blit(score,(x,y))


bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bx_c=0
by_c=10
bs="ready"
bullet_state=bs

def isCollision(ex,ey,bx,by):
	dist=math.sqrt((math.pow(ex-bx,2))+(math.pow(ey-by,2)))
	if dist<27:
		return True
	else:
		return False





def fire_bullet(x,y):
	global bs
	bs="fire"
	screen.blit(bulletImg,(x+16,y+10))

def enemy(x,y,i):
	screen.blit(enemyImg[i],(x,y))


def player(x,y):
	screen.blit(playerImg,(x,y))








running =True
while running:
	screen.fill((0,0,0))
	screen.blit(background,(0,0))

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				px_c=-8
			if event.key==pygame.K_RIGHT:
				px_c=8
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				px_c=0
			if event.key==pygame.K_SPACE:
				if bs=="ready":
					bulletX=playerX
					bulletSound = mixer.Sound("laser.wav")
					bulletSound.play()
					fire_bullet(bulletX,bulletY)

				
			



	


	
	playerX+=px_c
	if playerX<=0:
		playerX=0
	elif playerX>=736:
		playerX=736

	

	if bulletY<=0:
		bulletY=480
		bs="ready"
	for i in range(num_of_enemies):
		if enemyY[i]>440:
			for j in range(num_of_enemies):
				enemyY[j]=2000
			game_over_text()
			break
		enemyX[i] += enemyX_change[i]
		if enemyX[i] <= 0:
			enemyX_change[i] = 4
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] >= 736:
			enemyX_change[i] = -4
			enemyY[i] += enemyY_change[i]
		# Collision
		collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			explosionSound = mixer.Sound("explosion.wav")
			explosionSound.play()
			bulletY = 480
			bullet_state = "ready"
			score_value += 1
			enemyX[i] = random.randint(0, 736)
			enemyY[i] = random.randint(50, 150)
		enemy(enemyX[i], enemyY[i], i)

	










	if bs is "fire":
		fire_bullet(bulletX,bulletY)
		bulletY-=by_c

	




	player(playerX,playerY)
	show_score(textX,testY)
	
	pygame.display.update()




