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





JOIN_BUTTON = None
QUIT_GAME_BUTTON = None
button_names = [JOIN_BUTTON, QUIT_GAME_BUTTON]



def buttons(x_pos, y_pos):
    for i in button_names:
        i.redraw_button()
        if i.click(x_pos, y_pos):
            if button_names[i] == JOIN_BUTTON:
                #send to server: Join game
                pass
            elif button_names[i] == QUIT_GAME_BUTTON:
                #send to server: Quit game
                pass
        
my_info = (WIN, colors["RED"], colors["PINK"], GAME_WIDTH, GAME_HEIGHT)

my_checker_info = []
for i in range(0, 12, 1):
    insert_info = [my_info[_] for _ in range(0, len(my_info))]
    insert_info.insert(1, (i+1))

    if i < 4:
        insert_info.append(((((my_info[3]/8)*i)*2)+((my_info[3]/8)/2)))
        insert_info.append((((my_info[4]/8)*5)+((my_info[4]/8)/2)))
    elif 4 <= i < 8:
        insert_info.append(((((((my_info[3]/8)*(i-4))*2)))+((my_info[3]/8)*1.5)))
        insert_info.append((((my_info[4]/8)*6)+((my_info[4]/8)/2)))
    else:
        insert_info.append(((((my_info[3]/8)*(i-8))*2)+((my_info[3]/8)/2)))
        insert_info.append((((my_info[4]/8)*7)+((my_info[4]/8)/2)))
    insert_info.append(colors["ORANGE"])
    my_checker_info.append(insert_info)

checkers = []
for i in range(0, len(my_checker_info), 1):
    info_1, info_2, info_3, info_4, info_5, info_6, info_7, info_8, info_9 = my_checker_info[i]
    checkers.append(checker(info_1, info_2, info_3, info_4, info_5, info_6, info_7, info_8, info_9))




def draw_checker(checker):
    #print("[DRAWING] Drawing checker pieces...")
    checker.redraw_checker()






def draw_background(WIN, WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT, footer_color = (255, 255, 255), divider_color = (0, 0, 0), background_board_color=(186, 140, 99), background_square_color=(0, 0, 0)):

    #print("[DRAWING] Drawing board color...")
    pygame.draw.rect(WIN, background_board_color, (0, 0, WIDTH, HEIGHT))
    #print("[DRAWING] Drawing footer...")
    pygame.draw.rect(WIN, footer_color, (0, GAME_HEIGHT, WIDTH, (HEIGHT-GAME_HEIGHT)))
    #print("[DRAWING] Drawing divider...")
    pygame.draw.rect(WIN, divider_color, (0, GAME_HEIGHT, WIDTH, (HEIGHT-GAME_HEIGHT)), 5)
    #print("[DRAWING] Drawing squares...")
    draw_bg_square(WIN, GAME_WIDTH, GAME_HEIGHT, background_square_color)




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
    #if pygame.mouse.get_pressed[0]:
    #    pass



    #print("[UPDATING] Updating display")
    draw_background(WIN, WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT, colors["WHITE"], colors["SILVER"], colors["WOOD"], colors["BLACK"])
    for i in checkers:
        draw_checker(i)
    pygame.display.update()
    #print("[UPDATING] Display updated.")
    
"""  
    test.redraw_button()
    test.click(101, 101)
    pygame.display.update()
"""