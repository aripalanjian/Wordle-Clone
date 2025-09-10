
class Settings:

    def __init__(self):
        self.caption = "Wordle - CtrlAltElite"
        self.size = self.width,self.height = 1050,700

        self.isOpen = False
        self.state = ""

        #colors
        self.black = (0,0,0)
        self.dark = (62,62,66)
        self.gray = (128,128,128)
        self.white = (255,255,255)
        self.green = (1,154,1)
        self.yellow = (255,196,37)
        self.red = (255,0,0)

        self.buttons = []

        #game constants
        self.attemptsCount = 0
        self.attempts = [[],[],[],[],[],[]]
        self.currentAttempt = self.attempts[0]
        self.currentAttemptBtn = []
        self.won = None
        
        self.dailyWord = ""
        self.wordsPlayed = []
        self.dailyWordPool = []
        self.OtherWordsPool = []
        self.AllWords = []
        self.badLetters = []
