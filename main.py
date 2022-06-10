import pygame
from Utils.bg_square import draw_bg_square
from Utils.checker import checker
from Utils.colors import colors
from Utils.buttons import button
pygame.init()

GAME_WIDTH = GAME_HEIGHT = WIDTH = 500
HEIGHT = WIDTH + 100


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

FONT = pygame.font.SysFont("Arial", 20)




def draw(WIN, WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT, footer_color = (255, 255, 255), divider_color = (0, 0, 0), background_board_color=(186, 140, 99), background_square_color=(0, 0, 0)):
    #print("[UPDATING] Display updating...")
    #print("[DRAWING] Drawing board color...")
    WIN.fill(background_board_color)
    #print("[DRAWING] Drawing footer...")
    pygame.draw.rect(WIN, footer_color, (0, GAME_HEIGHT, WIDTH, (HEIGHT-GAME_HEIGHT)))
    #print("[DRAWING] Drawing divider...")
    pygame.draw.rect(WIN, divider_color, (0, GAME_HEIGHT, WIDTH, (HEIGHT-GAME_HEIGHT)), 5)
    #print("[DRAWING] Drawing squares...")
    draw_bg_square(WIN, GAME_WIDTH, GAME_HEIGHT, background_square_color)

    pygame.display.update()
    #print("[UPDATING] Display updated.")


"""
test = button(WIN, 50, 50, 50, 50, (255, 0, 0), True, 5, (192, 192, 192), True, "Test", FONT, (0, 0, 0))
"""

clock = pygame.time.Clock()
FPS = 60
clock.tick(60)
#print(f"Running at {FPS} frames per second.")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
"""  
    test.redraw_button()
    test.click(101, 101)
    pygame.display.update()
"""
    
