class Network:
    def __init__(self, l=None):
        if l is None:
            self.firstlayer = None
            self.lastlayer = None
        else:
            self.firstlayer = l
            self.lastlayer = l.getLastLayer()

    def setLayers(self,layer):
        self.firstlayer = layer
        self.lastlayer = layer.getLastLayer()


    def backpropagation(self,output):
        return self.lastlayer.backPropagationErrorLast(output)

    def evaluate(self,inputs):
        return self.firstlayer.evaluate(inputs)

    def updateWeight(self, inputs):
        self.firstlayer.updateWeight(inputs)

    def train(self, setinput, setoutputs):
        output = self.evaluate(setinput)
        self.backpropagation(setoutputs)
        self.updateWeight(setinput)

