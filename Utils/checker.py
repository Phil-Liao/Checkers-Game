import functions
import pygame

class checker:
    def __init__(self, WIN, checker_id, checker_color, king_checker_color, GAME_WIDTH, GAME_HEIGHT, x, y, on_click_color=(255, 165, 0)):
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
        
    
    def redraw_checker(self):
        pygame.draw.circle(self.WIN, self.checker_color, (self.x, self.y), self.checker_radius)
        if (self.GAME_HEIGHT-self.y) == (self.GAME_HEIGHT/8/2):
            self.king_checker = True
        if self.king_checker:
            pygame.draw.circle(self.WIN, self.king_checker_color(self.x, self.y), self.king_checker_radius)
        if self.cursor_touched:
            pygame.draw.circle(self.WIN, self.on_click_color, (self.x, self.y), self.on_click_radius)
                    #print("[DRAWNG] Drawing the clicking orage circle...")


    def get_information(self):
        information = {"WIN":self.WIN, "checker_id":self.checker_id, "checker_color":self.checker_color, "GAME_WIDTH":self.GAME_WIDTH, "GAME_HEIGHT":self.GAME_HEIGHT, "checker_radius":self.checker_radius, "king_checker":self.king_checker, "king_checker_radius":self.king_checker_radius, 'x':self.x, 'y':self.y}
        #print(information)
        return information


    def move(self, cursor_x_1, cursor_y_1, cursor_x_2, cursor_y_2):
        x_pos_true = (self.x-(self.GAME_WIDTH/8/2)) < cursor_x_1 < (self.x+(self.GAME_WIDTH/8/2))
        y_pos_true = (self.y-(self.GAME_HEIGHT/8/2)) < cursor_y_1 < (self.x+(self.GAME_HEIGHT/8/2))
        if x_pos_true and y_pos_true:
            self.cursor_touched = True
            
        if self.cursor_touched:
            new_x, new_y = functions.closest_to_point(cursor_x_2, cursor_y_2, self.GAME_WIDTH, self.GAME_HEIGHT)
            #print(f"[CHANGING] Changing (x, y) from ({self.x}, {self.y}) to ({new_x}, {new_y})...")
            self.x, self.y = new_x, new_y
            self.cursor_touched = False
