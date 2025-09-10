import random, datetime
from bin.util.textbox import InputBox
from bin.util.button import Button

class EndScreen:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.active = False
        self.state = "End"
        self.playAgain = Button(text="Play Again", txtSize=50,color=self.settings.black, settings=settings, active=True, action=self._play_again_action)
        
    def render(self):
        if self.settings.won:
            message = InputBox.render_text("Congrats You Won!", 35, self.settings.white)
        else:
            message = InputBox.render_text(f"Sorry you lost...The right word was {self.settings.dailyWord}", 35, self.settings.white)

        self.screen.blit(message, message.get_rect(center = (self.screen.get_rect().center[0],self.screen.get_rect().center[1])))
        self.playAgain.setPos(self.screen.get_rect().center[0],self.screen.get_rect().center[1] + self.screen.get_rect().center[1] * 4 / 16)
        self.playAgain.render(self.screen)

    def _play_again_action(self):
        self._reset_game()
        self.settings.state = "Play"
        self.playAgain.active = False
    
    def _reset_game(self):
        self.settings.attemptsCount = 0
        self.settings.attempts = [[],[],[],[],[],[]]
        self.settings.currentAttempt = self.settings.attempts[0]
        self.settings.currentAttemptBtn = []
        self.settings.badLetters = []
        self.settings.won = None
        self.settings.wordsPlayed.append(self.settings.dailyWord[:])

        random.seed(int(datetime.datetime.today().timestamp()))
        while (self.settings.dailyWord in self.settings.wordsPlayed):
            randInt = random.randrange(0, len(self.settings.AllWords))
            self.settings.dailyWord = self.settings.AllWords[randInt]
        print(f"New Word: {self.settings.dailyWord}")
    
    def setActive(self):
        self.active = True
        self.playAgain.active = True

    def setInactive(self):
        self.active = False