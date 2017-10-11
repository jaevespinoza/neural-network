
class NeuronLayer:
    def __init__(self, n, number,pl = None,nl=None):
        self.previouslayer = pl
        self.number = number
        self.neurons = n
        self.nextlayer = nl
        self.firstneurons = n

    def backPropagationErrorLast(self, expected):
        for i in range(len(self.neurons)):
            error = expected[i] - self.neurons[i].getOutput()
            self.neurons[i].adjustDeltaWithError(error)
        if not self.isFirst():
            self.previouslayer.backPropagation()

    def backPropagation(self):
        for i in range(len(self.neurons)):
            error = 0.0
            for j in range(len(self.nextlayer.neurons)):
                error += self.nextlayer.neurons[j].weightlist[i]*self.nextlayer.neurons[j].getDelta()
            self.neurons[i].adjustDeltaWithError(error)
        if not self.isFirst():
            self.previouslayer.backPropagation()



    def evaluate(self, inputs):
        output = []
        for i in range(len(self.neurons)):
            output.append(self.neurons[i].evaluate(inputs))
        if self.isLast():
            return output
        else:
            return self.nextlayer.evaluate(output)


    def updateWeight(self, inputs):
        learning = 0.2
        for i in range(len(self.neurons)):
            self.neurons[i].adjustWeightWithInput(inputs,learning)
            self.neurons[i].adjustBiasUsingLearningRate(learning)
        if not self.isLast():
            self.nextlayer.updateWeight(self.getOutputs())


    def meanAbsoluteError(self, expected):
        error = 0.0
        for i in range(len(self.neurons)):
            error += abs(expected[i] - self.neurons[i].getOutput())
        return error/len(self.neurons)

    def meanAbsoluteError(self, expected):
        error = 0.0
        for i in range(len(self.neurons)):
            error += (expected[i] - self.neurons[i].getOutput())^2
        return error/len(self.neurons)




    ##funciones auxiliares
    def isLast(self):
        return self.nextlayer is None

    def toString(self):
        print "layer " + str(self.number)

    def getNeurons(self):
        return self.neurons

    def isFirst(self):
        return self.previouslayer is None

    def setnextLayer(self, nl):
        self.nextlayer = nl

    def setPreviousLayer(self,pl):
        self.previouslayer = pl

    def getNext(self):
        return self.nextlayer

    def getPrevious(self):
        return self.previouslayer

    def getOutputs(self):
        lista = []
        for i in range(len(self.neurons)):
            lista.append(self.neurons[i].getOutput())
        return lista

    def getLastLayer(self):
        if self.isLast():
            return self
        return self.nextlayer.getLastLayer()

    def getFirstNeurons(self):
        return self.firstneurons

