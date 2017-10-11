import random


class AlphabetBinary:
    def __init__(self):
        self.alpha = ["0","1"]

    def getRandomChar(self):
        rand = random.randint(0,1)
        return self.alpha[rand]