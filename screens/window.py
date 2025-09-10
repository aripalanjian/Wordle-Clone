import pygame
from bin.util.settings import Settings
from bin.util.button import Button
from bin.util.textbox import InputBox
from screens.landing import LandingScreen
from screens.play import PlayScreen
from screens.end import EndScreen

class Window:

    def __init__(self, settings=Settings()):

        self.settings = settings        
        self.screen = pygame.display.set_mode(self.settings.size, pygame.RESIZABLE)
        pygame.display.set_caption(self.settings.caption)

        self.frame = None
        self.LandingScreen = LandingScreen(self.screen, self.settings)
        self.PlayScreen = PlayScreen(self.screen, self.settings)
        self.EndScreen = EndScreen(self.screen, self.settings)
    
    def render(self):
        while self.settings.isOpen:
            screen_center = self.screen.get_rect().center[0],self.screen.get_rect().center[1]
            self._title()
            if self.frame != None and self.settings.state != self.frame.state:
                print(f'Switching mode to {self.settings.state}')
                self.frame.setInactive()
                self.frame = None

            if self.settings.state == "Landing":
                if self.LandingScreen.active == False:
                    self.LandingScreen.setActive()
                self.frame = self.LandingScreen
            elif self.settings.state == "Play":
                if self.PlayScreen.active == False:
                    self.PlayScreen.setActive()
                self.frame = self.PlayScreen
            elif self.settings.state == "End":
                if self.EndScreen.active == False:
                    self.EndScreen.setActive()
                self.frame = self.EndScreen

            if self.frame != None:
                self.frame.render()
            pygame.display.update()

    def _title(self):
        screen_center = self.screen.get_rect().center[0],self.screen.get_rect().center[1]
        game_name = InputBox.render_text(self.settings.caption, 50, self.settings.white)
        game_name_rect = game_name.get_rect(center = (screen_center[0], 0 + screen_center[1]/8))

        self.screen.fill(self.settings.dark)
        self.screen.blit(game_name, game_name_rect)