
from AlphabetBinary import *
import random

class GeneticAlg:
    def __init__(self, numberpop, size, alphabet, mutrate, r, sol):
        self.population = []
        self.population_number = numberpop
        self.size = size
        self.alphabet = alphabet
        self.mutation_rate = mutrate
        self.solution = sol
        self.r = r
        self.generation_number = 1


    def createPopulation(self):
        for i in range(self.population_number):
            str = ""
            for j in range(self.size):
                char_random = self.alphabet.getRandomChar()
                str += char_random
            self.population.append(str)


    def clearPop(self):
        self.population = []


    def fitness(self):
        fitness_list = []
        break_condition = False
        for i in range(len(self.population)):
            fit_number = 0
            #print self.population
            #print self.solution
            for j in range(len(self.solution)):
                if self.solution[j] == self.population[i][j]:
                    fit_number += 1
                    if fit_number == self.size:
                        print "Solucion encontrada " + str(self.population[i]) + " es igual a la solucion " + str(self.solution)
                        print "Generaciones necesitadas: " + str(self.generation_number)
                        break_condition = True
                        break

            if break_condition:
                fitness_list = []
                break

            fitness_list.append([self.population[i], fit_number])

        return fitness_list

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
            print normalized_list

            for i in range(len(normalized_list)):
                acumulated_fit += normalized_list[i][1]
                acum_list.append([normalized_list[i][0],acumulated_fit])

            print acum_list
            selected_list = []
            for j in range(len(acum_list)*2):
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

            final_list = []
            for i in range(len(selected_list)):
                final_list.append(selected_list[i][0])
            print final_list
            return final_list

    def mixingParents(self, list_parent):
        poll_mix = []
        for i in range(len(self.population)):
            pick_parent_one = list_parent[i*2]
            pick_parent_two = list_parent[(2*i)+1]
            random_index = random.randint(0,self.size-1)
            part_one = pick_parent_one[:random_index]
            part_two = pick_parent_two[random_index:]
            genemix = part_one + part_two
            list_string = []
            for j in range(len(genemix)):
                rand_mut = random.random()
                list_string = list(genemix)
                if rand_mut > self.mutation_rate:

                    randchar = self.alphabet.getRandomChar()
                    while randchar == list_string[j]:
                        randchar = self.alphabet.getRandomChar()
                    list_string[j] = randchar

            genechanged = "".join(list_string)
            poll_mix.append(genechanged)

        self.clearPop()
        self.population = poll_mix
        print self.population

    def algorithm(self):
        self.createPopulation()
        iterations = 10
        while iterations > 0:
            lists = self.fitness()
            if lists == []:
                break
            normalized_l = self.normalizeFitness(lists)
            self.mixingParents(normalized_l)
            self.generation_number+=1
            iterations -=1


setup = GeneticAlg(10, 5, AlphabetBinary(), 0.32, 0.30, "01010")
setup.algorithm()









