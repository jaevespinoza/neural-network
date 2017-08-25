from Neuron import *
from NeuronLayer import *
from Network import *
from NetworkCreator import *
'''
neur = Neuron(-1,0,0,[3,2,1])
neur2 = Neuron(-2,0,0,[2,-1,0])
neur3 = Neuron(0,1,1,[3,0])
neur4 = Neuron(0,1,2,[1,2])
neurlayer2 = NeuronLayer([neur3,neur4],number=2)
neurlayer = NeuronLayer([neur,neur2],number=1, nl=neurlayer2)

net = Network(neurlayer)

print net.evaluate([0,0,1])
'''
netc = NetworkCreator()
net = netc.createNet(2,[3,2],3,-5,5,-3,-3)
print net.evaluate([0,1,1])