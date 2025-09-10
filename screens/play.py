import pygame
from pygame.rect import Rect
from bin.util.textbox import InputBox
from bin.util.button import Button

class PlayScreen:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.active = False
        self.state = "Play"
        self.keyBtns = []
        self.__init_keyboard_btns()
        self.notAWord = None
        
    def render(self):
        screen_center = self.screen.get_rect().center[0],self.screen.get_rect().center[1]

        playInstruction = InputBox.render_text("Type letters on keyboard or click characters.", 20, self.settings.white)
        playInstructRect = playInstruction.get_rect(center = (screen_center[0], 2 * screen_center[1] - screen_center[1] * 3 / 32))
        
        for i in range(len(self.settings.attempts)):
            self.__render_attempt(i)
        
        self.__render_keys()
        if self.notAWord != None:
            rectSize = self.notAWord.get_rect().size
            notRect = self.notAWord.get_rect(center = (screen_center[0] - rectSize[0]/8 , 0 + screen_center[1] * 5 / 16))
            self.screen.blit(self.notAWord, notRect)
        self.screen.blit(playInstruction, playInstructRect)

    def setActive(self):
        self.active = True
        if len(self.keyBtns) != 0:
            for btn in self.keyBtns:
                btn.color = self.settings.gray
                btn.active = True
            self.enter.active = True
            self.delete.active = True

    def setInactive(self):
        self.active = False
        if len(self.keyBtns) != 0:
            for btn in self.keyBtns:
                btn.active = False
            self.enter.active = False
            self.delete.active = False
    
    def _key_action(self):
        print(f'Current Attempt: {"".join([x.plaintext for x in self.settings.currentAttempt])}')

    def __init_keyboard_btns(self):
        keys = ["Q","W","E","R","T","Y","U","I","O","P",
                "A","S","D","F","G","H","J","K","L",
                "Z","X","C","V","B","N","M"]
        for key in keys:
            keyButton = Button(text=key, txtSize=35, color=self.settings.gray, settings=self.settings, active=True, action=self._key_action)
            self.keyBtns.append(keyButton)

        for key in self.keyBtns:
            key.rect.size = self.keyBtns[1].rect.size

        self.enter = Button(text="Enter", txtSize=35, color=self.settings.gray, settings=self.settings, active=True, action=None)
        self.delete = Button(text="   <-", txtSize=35, color=self.settings.gray, settings=self.settings, active=True, action=None)

    def __render_keys(self):
        screen_center = self.screen.get_rect().center[0],self.screen.get_rect().center[1]
        screen_bottom = self.screen.get_rect().bottom

        row1 = ["Q","W","E","R","T","Y","U","I","O","P"]
        row2 = ["A","S","D","F","G","H","J","K","L"]
        row3 = ["Z","X","C","V","B","N","M"]
        for key in self.keyBtns:
            x,y = 0,0
            keyValue = key.plaintext
            padding = 4
            if keyValue in row1:
                index = row1.index(keyValue)
                x = screen_center[0] - (len(row1) / 2 * (key.rect.size[0] + padding)) + index * (key.rect.size[0] + padding)
                y =  screen_bottom - screen_center[1] * 17 / 32
            elif keyValue in row2:
                index = row2.index(keyValue)
                x = screen_center[0] - (len(row2) / 2 * (key.rect.size[0] + padding)) + index * (key.rect.size[0] + padding)
                y = screen_bottom - screen_center[1] * 12 / 32
            else:
                index = row3.index(keyValue)
                x = screen_center[0] - (len(row3) / 2 * (key.rect.size[0] + padding)) + index * (key.rect.size[0] + padding)
                y = screen_bottom - screen_center[1] * 7 / 32
            key.setPos(x,y)
            key.render(self.screen)

        key = self.keyBtns[1]
        self.delete.rect.size = self.enter.rect.size
        x_enter = screen_center[0] - ((len(row3) + 1) / 2 * (key.rect.size[0] + padding)) - self.enter.rect.size[0]/2 - padding/2
        x_delete = screen_center[0] - ((len(row3) + 1) / 2 * (key.rect.size[0] + padding)) + ( len(row3)) * (key.rect.size[0] + padding) + self.delete.rect.size[0]/2 + padding/2
        y = screen_bottom - screen_center[1] * 7 / 32
        self.enter.setPos(x_enter, y)
        self.delete.setPos(x_delete, y)

        self.enter.render(self.screen)
        self.delete.render(self.screen)


        
        #Add Enter and delete here

    def __render_attempt(self, i):
        screen_center = self.screen.get_rect().center[0],self.screen.get_rect().center[1]
        
        attempt = self.settings.attempts[i]
        
        rectSize = self.keyBtns[1].rect.size
        padding = 5

        keyCopy = self.keyBtns[1].rect.copy()
        for j in range(1,6):
            if len(attempt) < j:
                #print empty rect
                keyCopy.center = (screen_center[0] - (5 / 2 * (rectSize[0] + padding)) + (j-1) * (rectSize[0] + padding), #x
                                    0 + (i * 2 * padding) + screen_center[1] * (i + 4) / 8) #y
                pygame.draw.rect(surface=self.screen,rect=keyCopy, border_radius=5, color=self.settings.white, width=3)
            else:
                letter = attempt[j-1]
                letter.rect.width = self.keyBtns[1].rect.width
                x = screen_center[0] - (5 / 2 * (rectSize[0] + padding)) + (j-1) * (rectSize[0] + padding) #x
                y = 0 + (i * 2 * padding) + screen_center[1] * (i + 4) / 8 #y
                letter.setPos(x,y)
                letter.render(self.screen)
        
        