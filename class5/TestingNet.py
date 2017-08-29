import time

from NetworkCreator import *
import unittest2 as ut

class TestingNet(ut.TestCase):
    def testAnd(self):
        xlist = []
        ylist = []
        outputlist = []
        netc = NetworkCreator()
        net = netc.createNet(2, [2, 1], [2, 2], 1, 5, 1, 5)

        for i in range(1000000):
            x = random.randint(0, 1)
            y = random.randint(0, 1)
            xlist.append(x)
            ylist.append(y)
            if x & y == 1:
                outputlist.append(1)
            else:
                outputlist.append(0)

        for i in range(1000000):
            net.train([xlist[i], ylist[i]], [outputlist[i]])

        self.assertEqual(net.evaluate([0, 0]), [0])
        self.assertEqual(net.evaluate([0, 1]), [0])
        self.assertEqual(net.evaluate([1, 0]), [0])
        self.assertEqual(net.evaluate([1, 1]), [1])

    def testOr(self):
        xlist = []
        ylist = []
        outputlist = []
        netc = NetworkCreator()
        net = netc.createNet(2, [2, 1], [2, 2], 1, 5, 1, 5)

        for i in range(1000000):
            x = random.randint(0, 1)
            y = random.randint(0, 1)
            xlist.append(x)
            ylist.append(y)
            if x | y == 1:
                outputlist.append(1)
            else:
                outputlist.append(0)

        for i in range(1000000):
            net.train([xlist[i], ylist[i]], [outputlist[i]])

        self.assertEqual(net.evaluate([0, 0]), [0])
        self.assertEqual(net.evaluate([0, 1]), [1])
        self.assertEqual(net.evaluate([1, 0]), [1])
        self.assertEqual(net.evaluate([1, 1]), [1])

    def testXor(self):
        xlist = []
        ylist = []
        outputlist = []
        netc = NetworkCreator()
        net = netc.createNet(2, [2, 1], [2, 2], 1, 5, 1, 5)

        for i in range(1000000):
            x = random.randint(0, 1)
            y = random.randint(0, 1)
            xlist.append(x)
            ylist.append(y)
            if x ^ y == 1:
                outputlist.append(1)
            else:
                outputlist.append(0)

        for i in range(1000000):
            net.train([xlist[i], ylist[i]], [outputlist[i]])

        self.assertEqual(net.evaluate([0, 0]), [0])
        self.assertEqual(net.evaluate([0, 1]), [1])
        self.assertEqual(net.evaluate([1, 0]), [1])
        self.assertEqual(net.evaluate([1, 1]), [0])
