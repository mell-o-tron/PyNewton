import pygame
from time import sleep
import numpy as np
import math
from pygame.locals import *
import random
import itertools

def pixels(screen, color, pos, thickness):
    for i in range(-thickness, thickness):
        for j in range(-thickness, thickness):
            screen.fill(color, ((pos[0] + i, pos[1] + j), (1, 1)))

def plot(screen, winsize, thickness, f, scale):
    
    color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
    
    prev_pos = (0,0)
    
    for i in range (0, winsize):
        pos = (i, winsize/2 - scale * (f((1/scale) * (i - winsize/2))))
        if i != 0:
            pygame.draw.line(screen, color,prev_pos,pos, thickness)
        prev_pos = pos
        #pixels(screen, color, pos, thickness)
        
    


def drawAxis(winsize, screen, axis_thickness):
    p = [[0, winsize/2], 
        [winsize, winsize/2], 
        [winsize/2, 0], 
        [winsize/2, winsize]]
    
    pygame.draw.line(screen, (255, 255, 255),p[0],p[1], axis_thickness)
    pygame.draw.line(screen, (255, 255, 255),p[2],p[3], axis_thickness)



def newton_iter(f, f1, x0, screen, winsize, thickness, scale):
    x = x0
    if f1(x) == 0:
        return 
    
    t = lambda y : (y-x)*f1(x)+f(x)
    plot(screen, winsize, thickness, t, scale)
    x = x - f(x) / f1(x)
    return x



def runPG(f, f1, x, scale, stop):
    winsize = 500
    axis_thickness = 3
    # Set up the drawing window
    screen = pygame.display.set_mode([winsize, winsize])
    screen.fill((10, 10, 10))

    drawAxis(winsize, screen, axis_thickness)

    plot(screen, winsize, 2, f, scale)
    
    if f1(x) == 0:
        print("f'(x) = 0")
        pygame.quit()
        return
        
    while abs(f(x)) > stop:
        x = newton_iter(f, f1, x, screen, winsize, 1, scale)
        print(f(x))
        pygame.display.flip()
        sleep(1)
        
    # Flip the display
    pygame.display.flip()
        
    pygame.quit()

