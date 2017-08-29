from SigmoidNeuron import *
import matplotlib.pyplot as plt
import random
from class3.Equation import Equation

xlist = []
ylist = []
outputlist = []
weight1list = []
weight2list = []
iterationlist = range(1000)
eq = Equation(3,-4)
misslist = []
miss = 0
error = 0.0
perc = SigmoidNeuron(1, 1, -1, 0.5)
for i in range(10000):
    x = random.randint(-50,50)
    y = random.randint(-50,50)
    xlist.append(x)
    ylist.append(y)
    calculatey = eq.eval(x)
    if calculatey <= y:
        outputlist.append(1)
    else:
        outputlist.append(0)

for i in range(10000):
    perc.learn(xlist[i], ylist[i], outputlist[i])
    weight1list.append(perc.getWeight1())
    weight2list.append(perc.getWeight2())

plt.figure(1)
plt.subplot(121)
plt.plot([-50,50], [3*-50 - 4, 3*50 - 4])
for i in range(500):
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    evaluation = perc.calculate(x,y)
    if evaluation == 1:
        plt.plot(x, y,"ro")
    else:
        plt.plot(x, y, "bo")
plt.show()