from random import random, randint, choice
from copy import deepcopy

import matplotlib.pyplot as plt

from tarea4.Node import Node
from tarea4.Number import Number
from tarea4.Variable import Variable


class ATS:
  def __init__(self, funwrappers, variables, numbers, checkdata,
               minimaxtype="min", population=None, size=10, maxdepth=10,
               maxgen=100, crossrate=0.9, mutationrate=0.1, newbirthrate=0.6):
    self.funwraplist = funwrappers
    self.variablelist = variables
    self.constantlist = numbers
    self.checkdata = checkdata
    self.minimaxtype = minimaxtype
    self.maxdepth = maxdepth
    self.population = population or self.createpopulation(size)
    self.size = size
    self.maxgen = maxgen
    self.crossrate = crossrate
    self.mutationrate = mutationrate
    self.newbirthrate = newbirthrate

    self.besttree = self.population[0]
    for i in range(0, self.size):
      self.population[i].depth=self.population[i].refreshdepth()
      self.population[i].getfitness(checkdata)
      if self.minimaxtype == "min":
        if self.population[i].fitness < self.besttree.fitness:
          self.besttree = self.population[i]
      elif self.minimaxtype == "max":
        if self.population[i].fitness > self.besttree.fitness:
          self.besttree = self.population[i]

  def createpopulation(self, popsize):
    return [self.createtree(0) for i in range(0, popsize)]


  def createtree(self, startdepth):
    if startdepth == 0:
      # hacer un arbol nuevo
      node_choose = 0 # el nodo a hacer primero es funcion siempre
    elif startdepth == self.maxdepth:
      node_choose = 1 # si estamos al final del arbol, solamente deben ser numeros
    else:
      node_choose = randint(0, 1) #si estamos al medio, se hace randommente
    if node_choose == 0: #si es funcion, entonces:

      childlist = []
      select_fun = randint(0, len(self.funwraplist) - 1) #seleccionar funcion aleatoria
      for i in range(0, self.funwraplist[select_fun].childcount):
        child = self.createtree(startdepth + 1) #crear hijos nuevos
        childlist.append(child)
      return Node("function", childlist, self.funwraplist[select_fun])

    else:
      if randint(0, 1) == 0: #retornamos variable
        select_variable = randint(0, len(self.variablelist) - 1) #seleccionar de la lista de variables
        return Node("variable", None, None,
               Variable(self.variablelist[select_variable]), None)
      else: #retornamos constante o numero
        select_constant = randint(0, len(self.constantlist) - 1) #seleccionar de la lista de constantes
        return Node("number", None, None, None,
               Number(self.constantlist[select_constant]))

  def mutate(self, tree, startdepth=0):
    #no mutar el arbol si es que es menor que mutate
    if random() < self.mutate:
      return self.createtree(startdepth)
    else:
      result = deepcopy(tree) #hacer una copia
      if result.type == "function": #hacer copia de los hijos tambien
        result.children = [self.mutate(c, startdepth + 1) \
                           for c in tree.children]
    return result

  def crossover(self, tree1, tree2, probswap=0.8, top=1):
    #si el random es menor a la probabilidad de cambiar
    if random() < probswap and not top:
      return deepcopy(tree2)
    else: # se hace copia de arbol 1
      result = deepcopy(tree1)
      if tree1.type == "function" and tree2.type == "function":
        #si ambos son funciones se debe hacer un crossover de los hijos
        result.children = [self.crossover(c, choice(tree2.children),
                           probswap, 0) for c in tree1.children]
    return result

  def envolve(self):
    fitness_list = []
    for i in range(0, self.maxgen):
      print "generation no.", i
      child = []
      for j in range(0, int(self.size * self.newbirthrate / 2)):
        #escoger 2 padres y crear un hijo nuevo
        parent1, p1 = self.randomselection()
        parent2, p2 = self.randomselection()
        new_child = self.crossover(parent1, parent2) #generar crossover entre 2 arboles
        child.append(new_child) # generar arbol nuevo
        parent, p3 = self.randomselection()
        newchild = self.mutate(parent) #mutar el arbol segun otro padre
        child.append(new_child)

      #actualizar el fitness de cada arbol
      for j in range(0, int(self.size * self.newbirthrate)):
        replacedtree, replacedindex = self.randomselection(reverse=True)

        #se reemplazan arboles malos con los hijos
        self.population[replacedindex] = child[j]

      #cambiar al mejor arbol segun fitness

      for k in range(0, self.size):
        self.population[k].getfitness(self.checkdata)
        self.population[k].depth=self.population[k].refreshdepth()
        if self.minimaxtype == "min":
          if self.population[k].fitness < self.besttree.fitness:
            self.besttree = self.population[k]
        elif self.minimaxtype == "max":
          if self.population[k].fitness > self.besttree.fitness:
            self.besttree = self.population[k]
      fitness_list.append(self.besttree.fitness)
      print "best tree's fitbess..",self.besttree.fitness
      if self.besttree.fitness == 0 and self.minimaxtype=="min":
        break

    self.besttree.display()
    plt.plot(range(self.maxgen), fitness_list)
    plt.xlabel("Generaciones")
    plt.ylabel("Fitness level")
    plt.show()

  #seleccionar un arbol aleatoriamente segun fitness
  def randomselection(self, reverse=False):
    if reverse == False:
      allfitness = 0
      for i in range(0, self.size):
        allfitness += self.population[i].fitness
      randomnum = random()*(self.size - 1)
      check = 0
      for i in range(0, self.size):
        check += (1.0 - self.population[i].fitness / allfitness)
        if check >= randomnum:
          return self.population[i], i
    if reverse == True:
      allfitness = 0
      for i in range(0, self.size):
        allfitness += self.population[i].fitness
      randomnum = random()
      check = 0
      if allfitness != 0:
        for i in range(0, self.size):
          check += self.population[i].fitness * 1.0 / allfitness
          if check >= randomnum:
            return self.population[i], i
