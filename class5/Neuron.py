class Neuron:
    def __init__(self, d, b, w = None):
        if w is None:
            self.weightlist = []
        else:
            self.weightlist = w
        self.bias = b
        self.output = 0
        self.delta = d

    def evaluate(self, inputl):
        tot = 0
        for i in range(len(self.weightlist)):
            tot += self.weightlist[i]*inputl[i]

        if tot > 0:
            self.output = 1
            return 1
        else:
            return 0

    def adjustWeightWithInput(self,inputs,learning):
        for i in range(len(inputs)):
            self.weightlist[i] += learning*self.delta*inputs[i]



    def transferDerivative(self):
        return self.output*(1.0-self.output)

    def adjustBiasUsingLearningRate(self,learn):
        self.bias += (learn*self.delta)

    def adjustDeltaWithError(self,error):
        self.delta = error*self.transferDerivative()

    def getWeightatIndex(self,i):
        return self.weightlist[i]

    def getBias(self):
        return self.bias

    def getWeight(self):
        return self.weightlist

    def getDelta(self):
        return self.delta

    def setBias(self,b):
        self.bias = b

    def setWeightatIndex(self,i,w):
        self.weightlist[i] = w

    def setDelta(self,d):
        self.delta = d