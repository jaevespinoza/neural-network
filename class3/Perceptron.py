class Perceptron:
    def __init__(self,w1,w2,x,y,b):
        self.weight1 = w1
        self.weight2 = w2
        self.input1 = x
        self.input2 = y
        self.bias = b

    def getWeight1(self):
        return self.weight1

    def getWeight2(self):
        return self.weight2

    def setWeight1(self, w):
        self.weight1 = w

    def setWeight2(self, w):
        self.weight2 = w

    def setInput1(self,x):
        self.input1 = x

    def selfInput2(self,y):
        self.input2 = y

    def calculate(self):
        if self.weight1*self.input1 + self.weight2*self.input2 + self.bias > 0:
            return 1
        else:
            return 0

    def printWeight(self):
        print "weight1: " + str(self.weight1) + ", weight2: " + str(self.weight2)