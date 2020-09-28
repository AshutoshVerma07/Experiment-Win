import pygame
from pygame.locals import*
pygame.init()
compsize = [pygame.display.Info().current_w , pygame.display.Info().current_h]
screen = pygame.display.set_mode((800 , 600) , pygame.RESIZABLE)
background = pygame.image.load('Background.png')
background_cor = [0 ,0]
fullscreen = False
running = True

while running:
    screen.fill((0 , 0 , 0))
    screen.blit(background , background_cor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(compsize , pygame.FULLSCREEN)
                    background = pygame.transform.scale(background , (compsize[1] , compsize[1]))
                    background_cor [0] = (compsize [0] - compsize [1]) / 2
                else:
                    screen = pygame.display.set_mode((800 , 600) , pygame.RESIZABLE)
                    background_cor [0] = 0
    pygame.display.update()