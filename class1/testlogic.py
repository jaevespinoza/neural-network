import unittest
from nand import *

class TestLogicPerceptons(unittest.TestCase):

    def test_nand(self):
        nand1 = NandPercepton(1,1)
        nand2 = NandPercepton(1,0)
        nand3 = NandPercepton(0,1)
        nand4 = NandPercepton(0,0)
        
        self.assertEquals(nand1.execute(),0)
        self.assertEquals(nand2.execute(),1)
        self.assertEquals(nand3.execute(),1)
        self.assertEquals(nand4.execute(),1)

    def test_or(self):
		or1 = OrPercepton(1,1)
		or2 = OrPercepton(1,0)
		or3 = OrPercepton(0,1)
		or4 = OrPercepton(0,0)
        
		self.assertEquals(or1.execute(),1)
		self.assertEquals(or2.execute(),1)
		self.assertEquals(or3.execute(),1)
		self.assertEquals(or4.execute(),0)
        

    def test_and(self):
		and1 = AndPercepton(1,1)
		and2 = AndPercepton(1,0)
		and3 = AndPercepton(0,1)
		and4 = AndPercepton(0,0)
        
		self.assertEquals(and1.execute(),1)
		self.assertEquals(and2.execute(),0)
		self.assertEquals(and3.execute(),0)
		self.assertEquals(and4.execute(),0)
        

if __name__ == '__main__':
    unittest.main()
