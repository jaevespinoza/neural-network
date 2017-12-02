class Number:
  def __init__(self, value):
    self.value = value
    self.name = str(value)
    self.type = "number"

  def evaluate(self):
    return self.value

  def display(self, indent=0):
    print (' '*indent), self.value