from class5.NetworkCreator import *
import matplotlib.pyplot as plt
from class5.Normal import *


net = NetworkCreator()
trueinput = []
trueoutput = []
pokernet = net.createNet(3, [9,7,9], [9, 9, 7], -3, 3, -1, 1)
m = 0


epochs = 1000



file_result = open("result.txt","w")
for i in range(epochs):
    file_red = open("tictactoe.txt", "r")
    filelist = file_red.readlines()
    for line in filelist:
        splitter = line.split(",")
        input = splitter[0:9]
        trueinput = transformArray(input)
        ls = splitter[9].replace("\n", "")
        output = transformInList(ls)
        inputs = normalizeInput(trueinput)
        pokernet.train(inputs,output)
        m += 1
        if m == 333:
            break

        splitterother = filelist[m+625].split(",")
        input = splitterother[0:9]
        trueinput = transformArray(input)
        ls = splitterother[9].replace("\n", "")
        output = transformInList(ls)
        inputs = normalizeInput(trueinput)
        pokernet.train(inputs,output)
        trueinput = []
        trueoutput = []

    file_red.close()
    m=0

    file_red = open("tictactoe.txt", "r")
    miss = 0.0
    for line in file_red:
        splitter = line.split(",")
        input = splitter[0:9]
        trueinput = transformArray(input)
        inputs = normalizeInput(trueinput)
        ls = splitter[9].replace("\n", "")
        output = transformInList(ls)
        result = approx(pokernet.evaluate(inputs))
        if result != output:
            miss += 1.0
    file_red.close()
    file_result.write(str(miss/958.0) + "\n")

    print "--- miss percentage: " + str(miss/958.0)

file_result.close()

pokernet.printChanges()

lista = []
file_read = open("result.txt","r")
for i in file_read:
    lista.append(float(i.replace("\n","")))
plt.plot(range(epochs), lista)
plt.show()

