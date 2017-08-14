from math import exp


class SigmoidNeuron:
    def __init__(self,w1,w2,b,t):
        self.weight1 = w1
        self.weight2 = w2
        self.bias = b
        self.threshold = t

    def getWeight1(self):
        return self.weight1

    def getWeight2(self):
        return self.weight2

    def setWeight1(self, w):
        self.weight1 = w

    def setWeight2(self, w):
        self.weight2 = w

    def calculate(self, x, y):
        sum = self.weight1*x + self.weight2*y + self.bias
        expon = exp(sum*-1)
        if 1/(1+expon) > self.threshold:
            return 1
        else:
            return 0

    def printWeight(self):
        print "weight1: " + str(self.weight1) + ", weight2: " + str(self.weight2)

    def learn(self,x,y,real):
        calculatedout = self.calculate(x, y)

        if calculatedout == 0 and real == 1:
            self.setWeight1(self.getWeight1() + 0.01 * x)
            self.setWeight2(self.getWeight2() + 0.01 * y)
        elif calculatedout == 1 and real == 0:
            self.setWeight1(self.getWeight1() - 0.01 * x)
            self.setWeight2(self.getWeight2() - 0.01 * y)