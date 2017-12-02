import random

from tarea4.ATS import ATS
from tarea4.FunWrapper import FunWrapper


def sumar(values):
    sumtotal = 0
    for val in values:
      sumtotal = sumtotal + val
    return sumtotal

def restar(values):
    return values[0] - values[1]

def multiplicar(values):
    return values[0] * values[1]

def dividir(values):
    if values[1] == 0:
        return 1
    return values[0] / values[1]

addwrapper = FunWrapper(sumar, 2, "sumar")
subwrapper = FunWrapper(restar, 2, "restar")
mulwrapper = FunWrapper(multiplicar, 2, "multiplicar")
divwrapper = FunWrapper(dividir, 2, "dividir")

def funcionejemplo(x):
  return (x*x) + x + 1

def constructcheckdata(count=10):
    checkdata = []
    for i in range(0, count):
        dic = {}
        x = random.randint(0, 10)
        dic['x'] = x
        dic['result'] = funcionejemplo(x)
        checkdata.append(dic)
    return checkdata

checkdata = constructcheckdata()
env = ATS([addwrapper, subwrapper, mulwrapper], ["x"],
                    [-3, -2, -1, 1, 2, 3], checkdata)
env.envolve()