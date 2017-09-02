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

    def printChanges(self):
        firstl = []
        first = self.firstlayer
        while first is not None:
            firstl.append(first.getNeurons())
            first = first.getNext()
        for i in range(len(firstl)):
            print "layer " + str(i)
            for j in range(len(firstl[i])):
                print "node " + str(j)
                old = firstl[i][j].getOld()
                new = firstl[i][j].getWeight()
                for k in range(len(old)):
                    print "weight " + str(k)
                    print old[k], new[k]
                print "----------- pesos completado ------------ "
            print "------------ nodos completados --------------"
        print "----------- layer completado -----------------"

