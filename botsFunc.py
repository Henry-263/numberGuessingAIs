import random

#Bot random1, devuelve numero aleatorio(se repiten numeros)
def random_bot1(_,maxNum):
    intentos = 0
    num = random.randint(1, maxNum)
    val = 0
    while num != val:
        val = random.randint(1, maxNum)
        intentos += 1
    return intentos

#Bot random2, devuelve numero aleatorio(no se repiten numeros)
def random_bot2(_,maxNum):
    intentos = 0
    num = random.randint(1, maxNum)
    val = 0
    listaVal = set()
    while num != val:
        while True:
            val = random.randint(1, maxNum)
            if val not in listaVal:
                break
        listaVal.add(val)
        intentos += 1
    return intentos

#Bot algoritmo, divide en mitad las posibilidades segun si es mayor o menor
def algoritmo_bot(_, maxNum):

    intentos = 1
    val = maxNum // 2
    max, min = maxNum + 1, 0
    num = random.randint(1, maxNum)

    while num != val:
        if val > num:
            max = val
        else:
            min = val
        val = (max + min) // 2
        intentos += 1
    return intentos

#LinealBot1 empieza en el 1 y va de uno en uno hasta encontrarlo
def linealBot1(_, maxNum):
    num = random.randint(1, maxNum)
    val = 1
    intentos = 1
    while True:
        if val == num:
            break
        else:
            val += 1
            intentos += 1
    return intentos