import pygame
from functions import is_odd




def draw_bg_square(WIN, GAME_WIDTH, GAME_HEIGHT, color=(0, 0, 0)):
    for y_axis in range(0, 8, 1):
        y_odd = is_odd(y_axis)
        for x_axis in range(0, 8, 1):
            x_odd = is_odd(x_axis)
            if (not(y_odd) and x_odd) or (y_odd and not(x_odd)):
                #print(f"Rectangle facts: Color = {color}, (x, y) = ({x_axis * 62.5}, {y_axis * 62.5}), GAME_WIDTH = {GAME_WIDTH / 8}, GAME_HEIGHT = {GAME_HEIGHT / 8}")    
                pygame.draw.rect(WIN, color, (x_axis * 62.5, y_axis * 62.5, GAME_WIDTH / 8, GAME_HEIGHT / 8))