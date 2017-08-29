from NetworkCreator import *
import time

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
xlist = []
ylist = []
outputlist = []
netc = NetworkCreator()
net = netc.createNet(2,[2,1],[2,2],1,5,1,5)

for i in range(1000000):
    x = random.randint(0,1)
    y = random.randint(0,1)
    xlist.append(x)
    ylist.append(y)
    if x|y == 1:
        outputlist.append(0)
    else:
        outputlist.append(1)

start_time = time.time()
for i in range(1000000):
    net.train([xlist[i],ylist[i]], [outputlist[i]])

print "--- %s seconds to train ---" % (time.time() - start_time)

print net.evaluate([1,1])
print net.evaluate([1,0])
print net.evaluate([0,1])
print net.evaluate([0,0])

