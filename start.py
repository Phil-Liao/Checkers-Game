import pygame
from Utils.colors import colors

def start_menu(WIN, FONT, FONT_COLOR, BG_COLOR=colors[WOOD]):
    WIN.fill(BG_COLOR)
    title_x = None
    title_y = None
    text = FONT.render("Chers Game by Phil Liao", True, FONT_COLOR) 
    textRect = text.get_rect()
    textRect.center = (title_x, title_y) 
    WIN.blit(text, textRect)

