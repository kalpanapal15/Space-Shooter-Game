
"""Pygame provides functions for creating programs with a graphical user interface,
or GUI (pronounced, “gooey”). Instead of a text-based CLI, programs with a graphics-based
GUI can show a window with images and colors."""
import pygame
import os


# loads the random module, which contains a number of random number generation-related functions.
import random

#extends the list of mathematical functions.
import math

#mixer pygame module for loading and playing sounds
from pygame import mixer

#new
FPS = 32

#initiaize mixer
mixer.init()

#initiaize pygame
pygame.init()

mixer.music.load('background.wav')
mixer.music.play(-1)

#screen size setting
screen_width =800
screen_height = 600
screen=pygame.display.set_mode((screen_width, screen_height))

#setting title and logo
pygame.display.set_caption("Space Shooter Game")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)


#load the background image
background=pygame.image.load('finalbg.png')

#load the spaceship i.e playerimage
spaceshipimg=pygame.image.load('playerimg.png')

#for adding multiple aliens
alienimg=[]
alienX=[]
alienY=[]
alienspeedX=[]
alienspeedY=[]

#no of aliens
no_of_aliens=10
#
def welcome_screen():
    pass
    while True:
        for event in pygame.eventget():
            if event.

#NEW
if __name__=="__main__":
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Space Shooter")
    main_screen=pygame.image.load("main screen.png")


#for loop for showing no of aliens
for i in range(no_of_aliens):
    alienimg.append(pygame.image.load('alien.png'))

    #position of aliens
    alienX.append(random.randint(0,736))
    alienY.append(random.randint(30,150))

    #speed parameters
    alienspeedX.append(-1)
    alienspeedY.append(15)


#initial score
score=0

#initial highscrore
highscore=0

#load the bullet image
bulletimg=pygame.image.load("bullet.png")
#setting the bullet_CENTER position
check=False
bulletX=380
bulletY=510

bulletimg2=pygame.image.load("bullet.png")
check=False
bulletX2=370
bulletY2=480

bulletimg3=pygame.image.load("bullet.png")
check=False
bulletX3=405
bulletY3=480


#set the player spaceship position
spaceshipX=370
spaceshipY=500
changeX=0
running=True

#setting font style and size for score
font=pygame.font.SysFont("Roboto" ,30, "bold")
#code for score visiblity
def score_text():
    img=font.render(f"Score: {score}",True,'White')
    screen.blit(img, (10,10))

#setting font style and size for highscore
font=pygame.font.SysFont("Roboto" ,30, "bold")
#code for score visiblity
def highscore_text():
    img=font.render(f"HighScore: {highscore}",True,'White')
    screen.blit(img, (600,10))



#setting font style and size for Game over
font_gameover=pygame.font.SysFont("Arial" ,64, "bold")

#code for game over visibility
def gameover_text():
    img_gameover=font_gameover.render("  GAME OVER",True,'Red')
    screen.blit(img_gameover, (200,250))

while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT: #if user press left arrow
                changeX=-1 #speed variable means it decide how fast,slow spaceship move

            if event.key==pygame.K_RIGHT:#if user press right arrow
                changeX=1

            if event.key==pygame.K_SPACE:
                if check is False:
                    bulletSound=mixer.Sound('laser.wav')
                    bulletSound.play()
                    check=True
                    bulletX=spaceshipX+16

            if event.key==pygame.K_SPACE:
                check=True
                bulletSound = mixer.Sound('laser.wav')
                bulletSound.play()
                check = True
                bulletX2 = spaceshipX + 2

            if event.key == pygame.K_SPACE:
                check = True
                bulletSound = mixer.Sound('laser.wav')
                bulletSound.play()
                check = True
                bulletX3 = spaceshipX + 30

        if event.type==pygame.KEYUP: #at rest position
            changeX=0
    spaceshipX+=changeX #spaceshipx = spaceshipx-changex
    #spaceship can not go out of left side
    if spaceshipX<=0:
        spaceshipX=0
    # spaceship can not go out of left side
    elif spaceshipX>=736:
        spaceshipX=736


    for i in range(no_of_aliens):
        #alien come close to spaceship
        if alienY[i]> 440:
            for j in range(no_of_aliens):
                # it will disappear
                alienY[j]= 2000
            gameover_text()
            gameover_sound = mixer.Sound('GAMEOVER.mp3')
            gameover_sound.play()
            break

        alienX[i]+=alienspeedX[i]
        if alienX[i]<=0:
            alienspeedX[i]=1
            alienY[i]+=alienspeedY[i]
        if alienX[i]>=736:
            alienspeedX[i]=-1
            alienY[i]+=alienspeedY[i]


        distance = math.sqrt(math.pow(bulletX - alienX[i], 2) + math.pow(bulletY - alienY[i], 2))
        if distance < 27:
            explosion = mixer.Sound('explosion.wav')
            explosion.play()
            bulletY = 500
            check = False
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(30, 150)
            score += 10
        screen.blit(alienimg[i], (alienX[i], alienY[i]))

        distance2 = math.sqrt(math.pow(bulletX2 - alienX[i], 2) + math.pow(bulletY2 - alienY[i], 2))
        if distance < 27:
            explosion = mixer.Sound('explosion.wav')
            explosion.play()
            bulletY2 = 500
            check = False
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(30, 150)
            score += 10
        screen.blit(alienimg[i], (alienX[i], alienY[i]))

        distance3 = math.sqrt(math.pow(bulletX3 - alienX[i], 2) + math.pow(bulletY3 - alienY[i], 2))
        if distance < 27:
            explosion = mixer.Sound('explosion.wav')
            explosion.play()
            bulletY3 = 500
            check = False
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(30, 150)
            score += 10
        screen.blit(alienimg[i], (alienX[i], alienY[i]))


    if bulletY<=0:
        bulletY=510
        check=False
    if check is True:
        screen.blit(bulletimg, (bulletX,bulletY))
        bulletY-=2


    if bulletY2<=0:
        bulletY2=480
        check=False
    #for bullet2 means left side bullet
    if check is True:
        screen.blit(bulletimg2, (bulletX2, bulletY2))
        bulletY2-=2

    if bulletY3<=0:
        bulletY3=480
        check=False
    # for bullet3 means RIGHT side bullet
    if check is True:
        screen.blit(bulletimg3, (bulletX3, bulletY3))
        bulletY3-= 2

    screen.blit(spaceshipimg, (spaceshipX, spaceshipY))
    score_text()
    highscore_text()
    pygame.display.update()

