import functions
import pygame


def closest_to_point(x, y, GAME_WIDTH, GAME_HEIGHT):
    GAME_WIDTH, GAME_HEIGHT = float(GAME_WIDTH), float(GAME_HEIGHT)
    for i in range(0, 9, 1):
        if i*(GAME_WIDTH/8) > x:
            x = (i*(GAME_WIDTH/8)) - ((GAME_WIDTH/8)/2)
            break
    for i in range(0, 9, 1):
        if i*(GAME_HEIGHT/8) > y:
            y = (i*(GAME_HEIGHT/8)) - ((GAME_HEIGHT/8)/2)
            break
    return x, y

class checker:
    def __init__(self, WIN, checker_id, checker_color, king_checker_color, GAME_WIDTH, GAME_HEIGHT, x, y, on_click_color):
        self.WIN = WIN
        self.checker_id = checker_id
        self.checker_color = checker_color
        self.king_checker_color = king_checker_color
        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.on_click_radius = GAME_WIDTH / 8 / 2
        self.on_click_color = on_click_color
        self.checker_radius = self.on_click_radius * 0.95
        self.king_checker = False
        self.king_checker_radius = self.checker_radius * 0.8
        self.x = x
        self.y = y
        self.cursor_touched = False

    def get_information(self):
        information = {"WIN":self.WIN, "checker_id":self.checker_id, "checker_color":self.checker_color, "GAME_WIDTH":self.GAME_WIDTH, "GAME_HEIGHT":self.GAME_HEIGHT, "checker_radius":self.checker_radius, "king_checker":self.king_checker, "king_checker_radius":self.king_checker_radius, 'x':self.x, 'y':self.y}
        #print(information)
        return information

    def unclick(self):
        self.cursor_touched = False
    def move(self, x, y):
        if not(self.cursor_touched):
            x_pos = (self.x-self.checker_radius) < x < (self.x+self.checker_radius)
            y_pos = (self.y-self.checker_radius) < y < (self.y+self.checker_radius)
            if x_pos and y_pos:
                self.cursor_touched = True
        elif self.cursor_touched:
            x_pos, y_pos = closest_to_point(x, y, self.GAME_WIDTH, self.GAME_HEIGHT)
            if (x_pos == self.x) and (y_pos == self.y):
                self.cursor_touched = False
            rqed_1 = (((abs(x_pos-self.x))%(self.GAME_WIDTH/8)) and (abs(y_pos-self.y)%(self.GAME_HEIGHT/8))) == 0
            rqed_2 = not(functions.is_odd((((abs(x_pos-self.x))/(self.GAME_WIDTH/8))+(abs(y_pos-self.y)/(self.GAME_HEIGHT/8)))))
            rqed_3 = (x_pos<self.GAME_WIDTH) and (y_pos<self.GAME_HEIGHT)

                    

            if rqed_1 and rqed_2 and rqed_3:
                self.x, self.y = x_pos, y_pos
                self.cursor_touched = False
                

    def check_king_checker(self):
        if self.y == (self.GAME_HEIGHT/8/2):
            self.king_checker = True

    def redraw_checker(self):
        pygame.draw.circle(self.WIN, self.checker_color, (self.x, self.y), self.checker_radius)
        if self.king_checker:
            pygame.draw.circle(self.WIN, self.king_checker_color, (self.x, self.y), self.king_checker_radius)
        if self.cursor_touched:
            pygame.draw.circle(self.WIN, self.on_click_color, (self.x, self.y), self.on_click_radius)
            #print(f"[DRAWNG] Drawing the clicking circle in the color of RGB({self.on_click_color})...")    
