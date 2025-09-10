import pygame
from bin.util.button import Button

class LandingScreen:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.active = False
        self.state = "Landing"
        self.play = Button(text="Play", txtSize=50,color=self.settings.black, settings=settings, active=True, action=self._play_action)
        
    def render(self):
        self.play.setPos(self.screen.get_rect().center[0],self.screen.get_rect().center[1])
        self.play.render(self.screen)

    def _play_action(self):
        self.settings.state = "Play"
        self.play.active = False

    def setActive(self):
        self.active = True
        self.play.active = True

    def setInactive(self):
        self.active = False
        