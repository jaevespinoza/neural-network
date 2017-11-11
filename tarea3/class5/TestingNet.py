import time

from NetworkCreator import *
import unittest2 as ut


def approx(out):
    if out > 0.7:
        return 1
    else:
        return 0

class TestingNet(ut.TestCase):
    def testAnd(self):
        netset = Network()
        neu1 = Neuron(0, 1, [2, 1])
        neu2 = Neuron(0, 2, [4, 3])
        neu3 = Neuron(0, 0, [1, 1])

        neur1 = NeuronLayer([neu1, neu2], 1)
        neur2 = NeuronLayer([neu3], 2, pl=neur1)
        neur1.setnextLayer(neur2)
        netset.setLayers(neur1)

        data = [[0, 0], [0, 1], [1, 0], [1, 1]]
        out = [[0], [0], [0], [1]]

        for i in range(10000):
            for j in range(len(data)):
                netset.train(data[j], out[j])

        self.assertEqual(approx(netset.evaluate([0, 0])[0]), 0)
        self.assertEqual(approx(netset.evaluate([0, 1])[0]), 0)
        self.assertEqual(approx(netset.evaluate([1, 0])[0]), 0)
        self.assertEqual(approx(netset.evaluate([1, 1])[0]), 1)

    def testOr(self):
        netset = Network()
        neu1 = Neuron(0, 1, [2, 1])
        neu2 = Neuron(0, 2, [1, 3])
        neu3 = Neuron(0, 0, [1, 1])

        neur1 = NeuronLayer([neu1, neu2], 1)
        neur2 = NeuronLayer([neu3], 2, pl=neur1)
        neur1.setnextLayer(neur2)
        netset.setLayers(neur1)

        data = [[0, 0], [0, 1], [1, 0], [1, 1]]
        out = [[0], [1], [1], [1]]

        for i in range(10000):
            for j in range(len(data)):
                netset.train(data[j], out[j])

        self.assertEqual(approx(netset.evaluate([0, 0])[0]), 0)
        self.assertEqual(approx(netset.evaluate([0, 1])[0]), 1)
        self.assertEqual(approx(netset.evaluate([1, 0])[0]), 1)
        self.assertEqual(approx(netset.evaluate([1, 1])[0]), 1)

    def testXor(self):
        netset = Network()
        neu1 = Neuron(0, 1, [2, 1])
        neu2 = Neuron(0, 2, [1, 3])
        neu3 = Neuron(0, 0, [1, 1])

        neur1 = NeuronLayer([neu1, neu2], 1)
        neur2 = NeuronLayer([neu3], 2, pl=neur1)
        neur1.setnextLayer(neur2)
        netset.setLayers(neur1)

        data = [[0, 0], [0, 1], [1, 0], [1, 1]]
        out = [[0], [1], [1], [0]]

        for i in range(10000):
            for j in range(len(data)):
                netset.train(data[j], out[j])

        self.assertEqual(approx(netset.evaluate([0, 0])[0]), 0)
        self.assertEqual(approx(netset.evaluate([0, 1])[0]), 1)
        self.assertEqual(approx(netset.evaluate([1, 0])[0]), 1)
        self.assertEqual(approx(netset.evaluate([1, 1])[0]), 0)
