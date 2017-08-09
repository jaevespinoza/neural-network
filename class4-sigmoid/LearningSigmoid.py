from SigmoidNeuron import *
import matplotlib.pyplot as plt
import random
from class3.Equation import Equation

perc = SigmoidNeuron(1,1,-1,0.5)
xlist = []
ylist = []
outputlist = []
weight1list = []
weight2list = []
iterationlist = range(1000)
eq = Equation(3,-4)
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
    calculatedout = perc.calculate(xlist[i-1],ylist[i-1])

    if calculatedout == 0 and outputlist[i-1] == 1:
        perc.setWeight1(perc.getWeight1() + 0.01*xlist[i-1])
        perc.setWeight2(perc.getWeight2() + 0.01*ylist[i-1])
    elif calculatedout == 1 and outputlist[i-1] == 0:
        perc.setWeight1(perc.getWeight1() - 0.01 * xlist[i - 1])
        perc.setWeight2(perc.getWeight2() - 0.01 * ylist[i - 1])
    perc.printWeight()
    weight1list.append(perc.getWeight1())
    weight2list.append(perc.getWeight2())

plt.plot([-50,50], [3*-50 - 4, 3*50 - 4], "k")
plt.grid(True, which='both')
for i in range(1000):
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    evaluation = perc.calculate(x,y)
    if evaluation == 1:
        plt.plot(x, y,"ro")
    else:
        plt.plot(x, y, "bo")
plt.show()