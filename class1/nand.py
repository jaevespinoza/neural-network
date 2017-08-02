
#class that represents the Nand Percepton
class NandPercepton:
	def __init__(self, x1, x2):
		self.first = x1
		self.second = x2
		self.weight_first = -2
		self.weight_second = -2
		self.bias = 3
		
	#execute percepton
	def execute(self):
		out = self.first*self.weight_first + self.second*self.weight_second + self.bias
		return out > 0
		
#class that represents the Or Percepton
class OrPercepton:
	def __init__(self, x1, x2):
		self.first = x1
		self.second = x2
		self.weight_first = 1
		self.weight_second = 1
		self.bias = 0
		
	#execute percepton
	def execute(self):
		out = self.first*self.weight_first + self.second*self.weight_second + self.bias
		return out > 0
		
#class that represents the And Percepton
class AndPercepton:
	def __init__(self, x1, x2):
		self.first = x1
		self.second = x2
		self.weight_first = 1
		self.weight_second = 2
		self.bias = -2
	
	#execute percepton
	def execute(self):
		out = self.first*self.weight_first + self.second*self.weight_second + self.bias
		return out > 0

		
		
	
