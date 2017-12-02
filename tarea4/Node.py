from PIL import Image, ImageDraw

class Node:
  def __init__(self, type, children, funwrap, var=None, const=None):
    self.type = type
    self.children = children
    self.funwrap = funwrap
    self.variable = var
    self.const = const
    self.depth = self.refreshdepth()
    self.value = 0
    self.fitness = 0

  def evaluate(self):
    result = 0
    if self.type == "variable":
      return self.variable.value
    elif self.type == "number":
      return self.const.value
    else:
      for c in self.children:
        result = [c.evaluate() for c in self.children]
      return self.funwrap.function(result)

    #get el fitness segun el checkdata
  def getfitness(self, checkdata):
    diff = 0
    for data in checkdata:
      self.setvariablevalue(data)
      diff += abs(self.evaluate() - data["result"])
    self.fitness = diff

    #setear valor para una variable en especifico
  def setvariablevalue(self, value):
    if self.type == "variable":
      if value.has_key(self.variable.var):
        self.variable.setvar(value[self.variable.var])
      else:
        print "There is no value for variable:", self.variable.var
        return
    if self.type == "number":
      pass
    if self.children: #si es que es una funcion, se deben ver los hijos
      for child in self.children:
        child.setvariablevalue(value)

    #actualizar la profundidad del arbol
  def refreshdepth(self):
    if self.type == "number" or self.type == "variable":
      return 0
    else:
      depth = []
      for c in self.children:
        depth.append(c.refreshdepth())
      return max(depth) + 1

  def __cmp__(self, other):
        return cmp(self.fitness, other.fitness)

  def display(self, indent=0):
    if self.type == "function":
      print ('  '*indent) + self.funwrap.name
    elif self.type == "variable":
      print ('  '*indent) + self.variable.name
    elif self.type == "number":
      print ('  '*indent) + self.const.name
    if self.children:
      for c in self.children:
        c.display(indent + 1)

