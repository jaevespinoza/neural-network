def normalizePosition(number):
    return [number/3, number%3]


def normalizeInputs(inputlist):
    lst = []
    for input in inputlist:
        if input == 'X':
            lst.append(0.0)
        elif input == 'O':
            lst.append(1.0)
        elif input == '0':
            lst.append(2.0)
    return lst

def transformToArray(number):
    lst = []
    for i in range(9):
        if i == number:
            lst.append("1.0")
        else:
            lst.append("0.0")
    return lst

def normalizeValue(value, datalow, datahigh, normallow, normalhigh):
    return ((value - datalow)*(normalhigh - normallow)/(datahigh - datalow)) + normallow


def denormalizeValue(value, datalow, datahigh, normallow, normalhigh):
    return ((datalow-datahigh)*value - (normalhigh*datalow) + datahigh*normallow)/(normallow - normalhigh)

def normalizeComplete(input):
    lst = []
    normallist = normalizeInputs(input)
    for inp in normallist:
        lst.append(normalizeValue(inp, 0.0, 2.0, 0.0, 1.0))
    return lst

def transformFloat(input):
    lst = []
    for i in input:
        lst.append(float(i))
    return lst