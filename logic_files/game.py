import pygame
import sys
import time
import random
import snake_game_logic as sgl

pygame.init()

resolution = (600, 600)
squares = 20

screen = pygame.display.set_mode(resolution)
font = pygame.font.SysFont('Arial', 30)

sgl.main_menu(screen, squares, resolution, font)
    
    

