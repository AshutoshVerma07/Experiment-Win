import random
import time
import pygame
import winsound

pygame.init()
running = True
pygame.display.set_caption("Experiment window")
font = pygame.font.Font("freesansbold.ttf", 25)
screen = pygame.display.set_mode((800 , 600))
img = pygame.image.load('C:\Users\JAY PRAKESH VERMA\Desktop\Ashutosh Verma\Char1.png')

#Actual Game Loop
while running:
    #Screen Render
    screen.fill((0 , 0 , 0))
    screen.blit(img , (100 , 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False