import unittest
from sumnand import *

class TestSumPerceptons(unittest.TestCase):

    def test_sum(self):
        sum1 = SumPercepton(1,1)
        sum2 = SumPercepton(1,0)
        sum3 = SumPercepton(0,1)
        sum4 = SumPercepton(0,0)
        
        dir1 = sum1.execute()
        dir2 = sum2.execute()
        dir3 = sum3.execute()
        dir4 = sum4.execute()
        
        ##first execution
        self.assertEquals(0, dir1['sum'])
        self.assertEquals(1, dir1['carry'])
        
        ##second execution
        self.assertEquals(1, dir2['sum'])
        self.assertEquals(0, dir2['carry'])
        
        ##third execution
        self.assertEquals(1, dir3['sum'])
        self.assertEquals(0, dir3['carry'])
        
        ##fourth execution
        self.assertEquals(0, dir4['sum'])
        self.assertEquals(0, dir4['carry'])
        

if __name__ == '__main__':
    unittest.main()
