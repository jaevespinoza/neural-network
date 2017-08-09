class Equation:
    def __init__(self,a,b):
        self.pendant = a
        self.constant = b

    def eval(self, input):
        return self.pendant*input + self.constant