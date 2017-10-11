
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

            for i in range(len(normalized_list)):
                acumulated_fit += normalized_list[i][1]
                acum_list.append([normalized_list[i][0],acumulated_fit])

            rand = 0.5
            selected_list = []
            for i in range(len(acum_list)):
                if acum_list[i][1] > rand:
                    break
                else:
                    selected_list.append(acum_list[i])

            final_list = []
            for i in range(len(selected_list)):
                final_list.append(selected_list[i][0])

            return final_list

    def mixingParents(self, list_parent):
        poll_mix = []
        for i in range(len(self.population)):
            genemix = ""
            pick_parent_one = random.randint(0, len(list_parent)-1)
            pick_parent_two = random.randint(0, len(list_parent)-1)
            random_index = random.randint(0,self.size-2)
            part_one = list_parent[pick_parent_one][:random_index]
            part_two = list_parent[pick_parent_two][random_index:]
            genemix += part_one + part_two
            genechanged = ""
            for j in range(len(genemix)):
                rand_mut = random.random()
                if rand_mut > self.mutation_rate:
                    list_string = list(genemix)

                    list_string[j] = self.alphabet.getRandomChar()

                    genechanged = "".join(list_string)
            poll_mix.append(genechanged)


        self.clearPop()
        self.population = poll_mix

    def algorithm(self):
        self.createPopulation()
        while True:
            lists = self.fitness()
            if lists == []:
                break
            normalized_l = self.normalizeFitness(lists)
            self.mixingParents(normalized_l)
            self.generation_number+=1


setup = GeneticAlg(20, 10, AlphabetBinary(), 0.32, 0.60, "0101001101")
setup.algorithm()









