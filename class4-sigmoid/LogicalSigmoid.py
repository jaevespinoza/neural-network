from SigmoidNeuron import *
import unittest2 as ut

class TestPerceptronSigmoid(ut.TestCase):
    def testAnd(self):
        AND = SigmoidNeuron(1,1,-1,0.5)
        self.assertEqual(AND.calculate(0,0),0)
        self.assertEqual(AND.calculate(1, 0),0)
        self.assertEqual(AND.calculate(0, 1),0)
        self.assertEqual(AND.calculate(1, 1),1)

    def testOr(self):
        OR = SigmoidNeuron(1,1,0,0.5)
        self.assertEqual(OR.calculate(0,0),0)
        self.assertEqual(OR.calculate(1, 0),1)
        self.assertEqual(OR.calculate(0, 1),1)
        self.assertEqual(OR.calculate(1, 1),1)

    def testNand(self):
        NAND = SigmoidNeuron(-2,-2,3,0.5)
        self.assertEqual(NAND.calculate(0,0),1)
        self.assertEqual(NAND.calculate(1, 0),1)
        self.assertEqual(NAND.calculate(0, 1),1)
        self.assertEqual(NAND.calculate(1, 1),0)
