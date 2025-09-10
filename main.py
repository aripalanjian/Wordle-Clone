import pygame
import threading, sys
from bin.util.settings import Settings
from bin.util.button import Button
from bin.util.textbox import InputBox
from screens.window import Window
import random, datetime

class Wordle:

    def __init__(self, debug=False):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        #Initialize Settings
        self.settings = Settings()
        self.settings.isOpen = True
        self.settings.state = "Landing"
        self._init_words()

        self.win = Window(self.settings)

        self.debug = debug

    def run(self) -> None:

        renderThread = threading.Thread(target=self.win.render)
        renderThread.start()
        print(f'Main Thread: Window is open {self.settings.isOpen}')
        while (self.settings.isOpen):
            #handle events
            self._check_events()

    def _init_words(self):
        with open('bin/dictionary/wordle-La.txt', 'r') as file:
            for line in file:
                self.settings.dailyWordPool.append(line.strip())

        with open('bin/dictionary/wordle-Ta.txt', 'r') as file:
            for line in file:
                self.settings.OtherWordsPool.append(line.strip())
        
        #Combine both sets so next word will be chosen from entire set of words
        self.settings.AllWords = self.settings.dailyWordPool + self.settings.OtherWordsPool
        #Randomly choose first word from daily words
        random.seed(int(datetime.datetime.today().timestamp()))
        randInt = random.randrange(0, len(self.settings.dailyWordPool))
        self.settings.dailyWord = self.settings.dailyWordPool[randInt]
        print(self.settings.dailyWord)
        

    def evaluateCurrentAttempt(self):
        attempt = ("".join([x.plaintext for x in self.settings.currentAttempt])).lower()
        word = self.settings.dailyWord.lower()
        if attempt not in self.settings.AllWords:
            self.win.PlayScreen.notAWord = InputBox.render_text("Not a word", 35, self.settings.white)
        elif attempt == word:
            for letter in self.settings.currentAttempt:
                letter.color = self.settings.green
            self.settings.won = True
            self.settings.state = "End"
            #go to win screen
        else:
            for i in range(len(self.settings.currentAttempt)):
                letter = self.settings.currentAttempt[i]
                letterText = letter.plaintext.lower()
                if letterText in word:
                    print(f"letter {letterText} in {word}")
                    if i == word.index(letterText):
                        letter.color = self.settings.green
                    else:
                        letter.color = self.settings.yellow
                else:
                    print(f"letter {letterText} not in {word}")
                    letter.color = self.settings.red
                    self.settings.badLetters.append(letterText)
                    for key in self.win.PlayScreen.keyBtns:
                        if key.plaintext == letter.plaintext:
                            key.color = self.settings.red
                            key.active = False
            
            self.settings.attemptsCount += 1
            if self.settings.attemptsCount > 5:
                self.settings.won = False
                self.settings.state = "End"
            else:
                self.settings.currentAttempt = self.settings.attempts[self.settings.attemptsCount]
        pass

    """Event Section"""
    def _check_events(self):
        #Watches for events then goes to appropriate function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings.isOpen = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_events()
            # elif event.type == pygame.KEYDOWN:
            #     self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):        
        current = self.settings.currentAttempt
        state = self.settings.state
        badLetter = pygame.key.name(event.key).lower() in self.settings.badLetters
        if event.key == pygame.K_a:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_b:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_c:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_d:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_e:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_f:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_g:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_h:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_i:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_j:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_k:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_l:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_m:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_n:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_o:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_p:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_q:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_r:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_s:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_t:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_u:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_v:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_w:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_x:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_y:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_z:
            if len(current) < 5 and state == "Play" and not badLetter:
                current.append(Button(text=pygame.key.name(event.key).upper(), txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
        elif event.key == pygame.K_RETURN:
            if state == "Landing":
                self.win.LandingScreen._play_action()
            elif state == "Play" and len(current) == 5:
                self.evaluateCurrentAttempt()
            elif state == "End":
                self.win.EndScreen._play_again_action()
        elif event.key == pygame.K_BACKSPACE:
            if len(current) > 0:
                current.pop()
            if self.win.PlayScreen.notAWord != None:
                self.win.PlayScreen.notAWord = None
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()

            

    def _check_mouse_events(self):
        """Responds to mouse events"""
        pos = pygame.mouse.get_pos()

        for button in self.settings.buttons:
            if button.click(pos) and button.active:
                if self.settings.state == "Play":
                    current = self.settings.currentAttempt
                    print(f"Current word len: {len(current)}, is enter button {button.plaintext == "Enter"}")
                    if button.plaintext == "Enter":
                        if len(current) == 5:
                            self.evaluateCurrentAttempt()
                    elif button.plaintext == "   <-":
                        if len(current) > 0:
                            current.pop()
                        if self.win.PlayScreen.notAWord != None:
                            self.win.PlayScreen.notAWord = None
                    else:
                        if len(current) < 5:
                            current.append(Button(text=button.plaintext, txtSize=35, color=self.settings.gray, settings=self.settings, active=False))
                    
                if button.action != None:
                    button.action()
                print(f'{button.plaintext} clicked')

if __name__ == '__main__':
    Wordle().run()