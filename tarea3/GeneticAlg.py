from class5.NetworkCreator import *
from class5.Normal import *


class GeneticAlg:
    def __init__(self, numberpop, mutrate, numberlayer, accuracy):
        self.population = []
        self.population_number = numberpop
        self.mutation_rate = mutrate
        self.generation_number = 1
        self.number = numberlayer
        self.alphabet = NetworkCreator()
        self.accuracyneeded = accuracy
        self.accuracyforfirst = []
        self.accuracyforsecond = []


    def createPopulation(self):
        for i in range(self.population_number):
            newnet = self.alphabet.createNet(self.number, [9,10,1], [9, 9, 10], -3, 3, -1, 1)
            self.population.append(newnet)


    def clearPop(self):
        self.population = []


    def fitness(self):
        fitness_list = []
        for i in range(len(self.population)):
            self.evaluateAccuracy(self.population[i])
            if i == 1:
                self.accuracyforsecond.append(self.population[i].getAccuracy())
            elif i == 0:
                self.accuracyforfirst.append(self.population[i].getAccuracy())

            if self.population[i].accuracy > self.accuracyneeded:
                print "Solucion encontrada Red" + str(i) + " esima posee accuracy mayor a 0.7"
                print "Generaciones necesitadas: " + str(self.generation_number)
                fitness_list = []
                break

            fitness_list.append([self.population[i], self.population[i].accuracy])

        return fitness_list

    def evaluateAccuracy(self, red):
        epochs = 10
        m = 0
        miss = 0.0
        trueinput = []
        trueoutput = []
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
                red.train(inputs, output)
                m += 1
                if m == 333:
                    break

                splitterother = filelist[m + 625].split(",")
                input = splitterother[0:9]
                trueinput = transformArray(input)
                ls = splitterother[9].replace("\n", "")
                output = transformInList(ls)
                inputs = normalizeInput(trueinput)
                red.train(inputs, output)
                trueinput = []
                trueoutput = []

            file_red.close()
            m = 0

        file_red = open("tictactoe.txt", "r")
        for line in file_red:
            splitter = line.split(",")
            input = splitter[0:9]
            trueinput = transformArray(input)

            inputs = normalizeInput(trueinput)
            ls = splitter[9].replace("\n", "")
            output = transformInList(ls)
            result = approx(red.evaluate(inputs))
            if (output == [1,0] and result==[0]) or (output ==[0,1] and result==[1]):
                miss += 1.0
        file_red.close()
        red.setAccuracy(1.0 - (miss / 958.0))
        print red.accuracy

    def normalizeFitness(self, lists):
            normalizer_sum = 0.0
            normalized_list = []
            for i in range(len(lists)):
                normalizer_sum += lists[i][1]

            for i in range(len(lists)):
                number = lists[i][1]/normalizer_sum
                normalized_list.append([lists[i][0], number])

            normalized_list.sort(key=lambda fit:fit[1], reverse=True)
            acum_list = []
            acumulated_fit = 0.0

            for i in range(len(normalized_list)):
                acumulated_fit += normalized_list[i][1]
                acum_list.append([normalized_list[i][0],acumulated_fit])

            selected_list = []
            for j in range(len(acum_list)*2-2):
                rand = random.random()
                for i in range(len(acum_list)):
                    if acum_list[i][1] > rand:
                        if i == 0:
                            selected_list.append(acum_list[0])
                            break
                        else:
                            selected_list.append(acum_list[i-1])
                            break
                    else:
                        continue

            selected_list.append(acum_list[len(acum_list)-1])
            selected_list.append(acum_list[len(acum_list)-2])

            final_list = []
            for i in range(len(selected_list)):
                final_list.append(selected_list[i][0])
            return final_list



    def mixingParents(self, list_parent):
        poll_mix = []
        for i in range(len(self.population)):
            pick_parent_one = list_parent[i * 2]
            pick_parent_two = list_parent[(2 * i) + 1]

            nets = Network()

            nets.setFirstLayer(pick_parent_one.getFirst())
            nets.setLearning(pick_parent_two.getLearning())

            first = nets.firstlayer
            liss = []
            first_layer = pick_parent_one.firstlayer
            second_layer = pick_parent_two.firstlayer
            while first is not None:
                for k in range(len(first.neurons)):
                    for j in range(len(first.neurons[k].weightlist)):
                        rands = random.random()
                        if rands < self.mutation_rate:
                            weight = first_layer.neurons[k].weightlist[j]
                        else:
                            weight = second_layer.neurons[k].weightlist[j]

                        first.neurons[k].weightlist[j] = weight
                liss.append(first)
                first = first.getNext()
                first_layer = first_layer.getNext()
                second_layer = second_layer.getNext()
            for c in reversed(range(len(liss))):
                if c == self.number - 1:
                    liss[c].setPreviousLayer(liss[c - 1])
                elif c == 0:
                    liss[c].setnextLayer(liss[c + 1])
                else:
                    liss[c].setPreviousLayer(liss[c - 1])
                    liss[c].setnextLayer(liss[c + 1])

            nets.setLayers(liss[0])

            poll_mix.append(nets)

        self.clearPop()
        self.population = poll_mix

    def algorithm(self):
        self.createPopulation()
        iterations = 1
        while iterations <= 20:
            lists = self.fitness()
            if lists == []:
                break

            normalized_l = self.normalizeFitness(lists)
            self.mixingParents(normalized_l)
            self.generation_number+=1
            iterations +=1
            print "------ new generation --------"
        '''
        plt.subplot(2, 1, 1)
        plt.plot(range(len(self.accuracyforfirst)), self.accuracyforfirst, 'k')
        plt.title('Evolucion de primera red')
        plt.ylabel('Accuracy')
        plt.xlabel('Iteraciones')

        plt.subplot(2, 1, 2)
        plt.plot(range(len(self.accuracyforsecond)), self.accuracyforsecond, 'k')
        plt.title('Evolucion de segunda red')
        plt.ylabel('Accuracy')
        plt.xlabel('Iteraciones')

        plt.show()
        '''

setup = GeneticAlg(10, 0.1,3, 0.7)
setup.algorithm()














