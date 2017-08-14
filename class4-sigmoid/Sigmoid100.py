import matplotlib.pyplot as plt
import random
from SigmoidNeuron import *

performance = []
def test100cases(perceptron, pnd, cnst):
    miss = 0.0
    for i in range(100):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        answer = 0
        if ((pnd*x) - cnst) >= y:
            answer = 1
        if (perceptron.calculate(x,y) != answer):
            miss +=1.0
    return (100-miss)/100

for i in range(500):
    sigmoid = SigmoidNeuron(1, 1, -1, 0.5)
    for k in range(i):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        out = 0
        eq = 3*x - 4
        if (eq < y):
            out = 1
        sigmoid.learn(x,y,out)
    performance.append(test100cases(sigmoid, 3, -4))

plt.plot(range(500), performance)
plt.show()




