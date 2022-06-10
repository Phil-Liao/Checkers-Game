import pygame

class button:
    def __init__(self, WIN, x, y, width, height, button_color, border=False, border_width=5, border_color=(192, 192, 192), add_text=False, text=None, FONT=None, text_color=(0, 0, 0)):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_color = button_color
        self.border = border
        if self.border:
            self.border_width = border_width
            self.border_color = border_color
        self.add_text = add_text
        if self.add_text:
            self.text = text
            self.FONT = FONT
            self.text_color = text_color

    def redraw_button(self):
        pygame.draw.rect(self.WIN, self.button_color, (self.x, self.y, self.width, self.height))
        if self.border:
            pygame.draw.rect(self.WIN, self.border_color, (self.x, self.y, self.width, self.height), self.border_width)
        if self.add_text:
            text = self.FONT.render(self.text, False, self.text_color)
            position = (self.x+(self.width//2), self.y+(self.height//2))
            self.WIN.blit(text, position)

    def click(self, cursor_x, cursor_y):
        button_area_x = self.x < cursor_x < self.x + self.width
        button_area_y = self.y < cursor_y < self.y + self.height
        if button_area_x and button_area_y:
            #print("[DETECTED] Clicked button.")
            return True
        else:
            #print("[DIDN'T DETECT] Didn't click the button.")
            return False