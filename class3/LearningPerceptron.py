from Equation import *
from Perceptron import *
import matplotlib.pyplot as plt
import random

perc = Perceptron(1,1,0,0,3)
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
    perc.setInput1(xlist[i-1])
    perc.selfInput2(ylist[i-1])

    calculatedout = perc.calculate()

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
for i in range(1000):
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    perc.setInput1(x)
    perc.selfInput2(y)
    evaluation = perc.calculate()
    if evaluation == 1:
        plt.plot(x, y,"ro")
    else:
        plt.plot(x, y, "bo")
plt.show()
#pl = plt.plot(iterationlist, weight1list)
#plt.show(pl)



