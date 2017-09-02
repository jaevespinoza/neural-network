def normalize(value, datalow,datahigh,normallow,normalhigh):
    return ((value - datalow)*(normalhigh - normallow)/(datahigh - datalow)) + normallow

def denormalize(value, datalow,datahigh,normallow,normalhigh):
    return ((datalow-datahigh)*value - (normalhigh*datalow) + datahigh*normallow)/(normallow - normalhigh)

def transformInList(letter):
    if letter == 'positive':
        return [1,0]
    else:
        return [0,1]
def approx(array):
    lista = []
    for i in array:
        if i > 0.7:
            lista.append(1)
        else:
            lista.append(0)
    return lista

def transformArray(array):
    lista = []
    for i in array:
        if i == 'x':
            lista.append(0.0)
        elif i == 'o':
            lista.append(1.0)
        elif i == 'b':
            lista.append(2.0)
    return lista

def normalizeInput(array):
    newarray = []
    for i in range(len(array)):
            newarray.append(normalize(array[i], 0.0, 2.0, 0.0, 1.0))
    return newarray