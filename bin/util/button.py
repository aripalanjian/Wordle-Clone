from pygame import draw, Rect
from bin.util.textbox import InputBox
#future added fuctionality
#https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
class Button:
    """Button Initializer"""
    def __init__(self, text="", txtSize=10, x=0, y=0, color=(128,128,128), active=False, settings=None, action=None):
        self.plaintext = text
        self.text = InputBox.render_text(text, txtSize, (255,255,255))
        self.rect = self.text.get_rect(center = (x, y))
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.padding = 10
        self.width = self.rect.width
        self.height = self.rect.height + self.padding
        self.active = active
        self.action = action
        if settings != None:
            settings.buttons.append(self)
        

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y        
        self.rect.center = (self.pos_x, self.pos_y)
        
    def render(self, screen):
        """Draws button to screen"""
        draw.rect(screen, self.color, self.rect, border_radius=5)
        screen.blit(self.text, self.rect)

    def click(self,pos):
        """Detects if click within bounds of button"""
        x = pos[0]
        y = pos[1]
        if (self.pos_x - self.width/2) <= x <= (self.pos_x + self.width/2) and (self.pos_y - self.height/2)  <= y <= (self.pos_y + self.height/2):
            return True
        else:
            return False
        
    def recenter(self):
        self.width = self.rect.width
        self.height = self.rect.height + self.padding