import pygame
from Utils.bg_square import draw_bg_square
from Utils.checker import checker
from Utils.colors import colors
from Utils.buttons import button

pygame.init()
pygame.font.init()

GAME_WIDTH = GAME_HEIGHT = WIDTH = 500
HEIGHT = WIDTH + 100


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

FONT = "Arial"
MAIN_FONT = pygame.font.SysFont(FONT, 24)
TITLE_FONT = pygame.font.SysFont(FONT, 30)

phase = 1

my_info = (WIN, colors["RED"], colors["PINK"], GAME_WIDTH, GAME_HEIGHT)
opp_info = (WIN, colors["GRAY"], colors["SILVER"], GAME_WIDTH, GAME_HEIGHT)


my_checker_info = []
for i in range(0, 12, 1):
    insert_info = [my_info[_] for _ in range(0, len(my_info), 1)]
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
#print(my_checker_info)
my_checkers = []
for i in range(0, len(my_checker_info), 1):
    info_1, info_2, info_3, info_4, info_5, info_6, info_7, info_8, info_9 = my_checker_info[i]
    my_checkers.append(checker(info_1, info_2, info_3, info_4, info_5, info_6, info_7, info_8, info_9))


opp_checker_info = []
for i in range(0, 12, 1):
    insert_info = [opp_info[_] for _ in range(0, len(opp_info), 1)]
    insert_info.insert(1, (i+1))
    if i < 4:
        insert_info.append(((((opp_info[3]/8)*i)*2)+((opp_info[3]/8)*1.5)))
        insert_info.append((((opp_info[4]/8)*0)+((opp_info[4]/8)/2)))
    elif 4 <= i < 8:
        insert_info.append((((((opp_info[3]/8)*(i-4)*2)))+((opp_info[3]/8)/2)))
        insert_info.append((((opp_info[4]/8)*1)+((opp_info[4]/8)/2)))
    else:
        insert_info.append(((((opp_info[3]/8)*(i-8))*2)+((opp_info[3]/8)*1.5)))
        insert_info.append((((opp_info[4]/8)*2)+((opp_info[4]/8)/2)))
    insert_info.append(colors["BROWN"])
    opp_checker_info.append(insert_info)
#print(opp_checker_info)
opp_checkers = []
for i in range(0, len(opp_checker_info), 1):
    info, info_2, info_3, info_4, info_5, info_6, info_7, info_8, info_9 = opp_checker_info[i]
    opp_checkers.append(checker(info, info_2, info_3, info_4, info_5, info_6, info_7, info_8, info_9))


def start_menu(WIN, WIDTH, HEIGHT, FONT_COLOR, FONT = TITLE_FONT, BG_COLOR=colors["WOOD"], TITLE_TEXT="Checkers Game by Phil Liao"):
    pygame.draw.rect(WIN, BG_COLOR, (0, 0, WIDTH, HEIGHT))
    text = FONT.render(TITLE_TEXT, True, FONT_COLOR)
    area = text.get_rect(center=(WIDTH/2, HEIGHT/8)) 
    WIN.blit(text, area)

def draw_background(WIN, WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT, footer_color = (255, 255, 255), divider_color = (0, 0, 0), background_board_color=(186, 140, 99), background_square_color=(0, 0, 0)):

    #print("[DRAWING] Drawing board color...")
    pygame.draw.rect(WIN, background_board_color, (0, 0, WIDTH, HEIGHT))
    #print("[DRAWING] Drawing footer...")
    pygame.draw.rect(WIN, footer_color, (0, GAME_HEIGHT, WIDTH, (HEIGHT-GAME_HEIGHT)))
    #print("[DRAWING] Drawing divider...")
    pygame.draw.rect(WIN, divider_color, (0, GAME_HEIGHT, WIDTH, (HEIGHT-GAME_HEIGHT)), 5)
    #print("[DRAWING] Drawing squares...")
    draw_bg_square(WIN, GAME_WIDTH, GAME_HEIGHT, background_square_color)

def draw_checker(my_checker, opp_checker):
    for i in my_checkers:
        i.redraw_checker()
        #print("[DRAWING] Drawing checker pieces...")
        i.check_king_checker()
        #print("[CHECKING] Checking if king checker.")
    for i in opp_checkers:
        i.redraw_checker()
        #print("[DRAWING] Drawing checker pieces...")


def click(x, y, my_checkers, phase=0):
    if phase == 0:
        pass
    elif phase == 1:
        collide = []
        remove = None




        for i in my_checkers:
            x_y = (i.get_information()['x'], i.get_information()['y'])
            collide.append(x_y)
        for i in my_checkers:
            remove = i.move(x, y, collide)



    else:
        pass


clock = pygame.time.Clock()
FPS = 60
clock.tick(60)
#print(f"Running at {FPS} frames per second.")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click(pos[0], pos[1], my_checkers, phase)
            

    if phase == 0:
        start_menu(WIN, WIDTH, HEIGHT, colors["BLACK"] , TITLE_FONT, colors["WOOD"], "Checkers Game by Phil Liao")
    elif phase == 1:
        #print("[UPDATING] Updating display")
        draw_background(WIN, WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT, colors["WHITE"], colors["SILVER"], colors["WOOD"], colors["BLACK"])
        draw_checker(my_checkers, opp_checkers)      
    else:
        pass
    pygame.display.update()
        #print("[UPDATING] Display updated.")
"""  
    test.redraw_button()
    test.click(101, 101)
    pygame.display.update()
"""