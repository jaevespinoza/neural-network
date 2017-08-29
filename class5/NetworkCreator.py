from Network import *
from NeuronLayer import *
from Neuron import *
import random

class NetworkCreator():
    def __init__(self):
        self.network = Network()

    def createNet(self, layernumber, listofneurons, listofweightnumber, range1,range2,bias1,bias2):
        layerl = []
        '''crear layer'''
        for i in range(layernumber):
            neuronl = []
            '''crear lista de neurones'''
            for j in range(listofneurons[i]):
                weightl = []

                for k in range(listofweightnumber[i]):
                    weight = random.randint(range1,range2)
                    weightl.append(weight)

                bias = random.randint(bias1,bias2)
                neuron = Neuron(0,bias,weightl)
                neuronl.append(neuron)

            layer = NeuronLayer(neuronl,i,None, None)
            layerl.append(layer)


        for i in reversed(range(layernumber)):
            if i==layernumber-1:
                layerl[i].setPreviousLayer(layerl[i-1])
            elif i==0:
                layerl[i].setnextLayer(layerl[i+1])
            else:
                layerl[i].setPreviousLayer(layerl[i-1])
                layerl[i].setnextLayer(layerl[i + 1])

        self.network.setLayers(layerl[0])
        return self.network


