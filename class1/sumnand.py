from nand import *

class SumPercepton:
	##constructor of the class
	def __init__(self,x1,x2):
		self.one = x1
		self.two = x2
	
	##execute the command sum
	def execute(self):
		##create the 5 nand perceptons necessary with the correct inputs
		nand1 = NandPercepton(self.one,self.two)
		result_nand1 = nand1.execute()
		
		nand2 = NandPercepton(self.one,result_nand1)
		result_nand2 = nand2.execute()
		
		nand3 = NandPercepton(self.two,result_nand1)
		result_nand3 = nand3.execute()
		
		nand4 = NandPercepton(result_nand1,result_nand1)
		result_nand4 = nand4.execute()
		
		nand5 = NandPercepton(result_nand2,result_nand3)
		result_nand5 = nand5.execute()
		
		##return a dictionary so you can return two values
		return {'sum': result_nand5, 'carry': result_nand4}
	
