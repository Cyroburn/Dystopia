#! /usr/bin/python3
import os
import sys
import math
import random
import pygame
from pygame.locals import *
#Pygame Var
pygame.display.set_caption('Dystopia')
display_resolution=(1024,576)
screen = pygame.display.set_mode((display_resolution), 0, 32)
display = pygame.Surface((512,428))
base_display = display.copy()
display.set_colorkey((0, 0, 0))
clock = pygame.time.Clock()
running = True
background_colour = (234, 212, 252)
#Function Var
TILE_SIZE = 16
PARALLAX = 0.5
#Function Call
player_sprite = load_img('data/img/player/man.png')


while running:
    #Layering
    screen.fill(background_colour)
    #World Logic
    #Physics?

    #Input Machine
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            #if event.key in [K_LEFT, K_a]:

            #if event.key in [K_RIGHT, K_d]:

            #if event.key in [K_w, K_UP]:

            #if event.key in [K_s, K_DOWN]:


    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(45)
