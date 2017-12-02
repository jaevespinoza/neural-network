class Variable:
  def __init__(self, var, value=0):
    self.var = var
    self.value = value
    self.name = str(var)
    self.type = "variable"

  def evaluate(self):
    return self.value

  def setvar(self, value):
    self.value = value

  def display(self, indent=0):
    print (' '*indent), self.var