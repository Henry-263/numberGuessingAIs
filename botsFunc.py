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

# Bot que elige numeros aleatorios dentro de rango minimo y maximo posible
def random_bot3(_,maxNum):
    intentos = 0
    num = random.randint(1, maxNum)
    val = 0
    maxPos = maxNum
    minPos = 1
    while num != val:
        val = random.randint(minPos, maxPos)
        if val > num:
            maxPos = val - 1
        else:
            minPos = val + 1
        intentos += 1
    return intentos

#Bot algoritmo, divide en mitad las posibilidades segun si es mayor o menor
def algoritmo_bot1(_, maxNum):

    intentos = 1
    val = maxNum // 2
    max, min = maxNum, 1
    num = random.randint(1, maxNum)

    while num != val:
        if val > num:
            max = val - 1
        else:
            min = val + 1
        val = (max + min) // 2
        intentos += 1
    return intentos

#Bot algoritmo, divide en 3 o 2/3
def algoritmo_bot2(_, maxNum):
    intentos = 0
    min, max = 1, maxNum
    num = random.randint(1, maxNum)

    while True:
        aleat = random.randint(1, 2)
        if aleat == 1:
            val = min + (max - min) // 3
        else:
            val = min + 2 * (max - min) // 3
        intentos += 1

        if val == num:
            return intentos
        elif val > num:
            max = val - 1
        else:
            min = val + 1

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

#LinealBot2 empieza al principio y al final y va subiendo y bajando: 1-100-2-99-3-98...
def linealBot2(_, maxNum):
    num = random.randint(1, maxNum)
    inicio = 1
    final = maxNum
    intentos = 1
    while True:
        if inicio == num or final == num:
            break
        else:
            if intentos % 2 == 0:
                inicio += 1
                intentos += 1
            else:
                final -= 1
                intentos += 1
    return intentos

#Salta de diez en diaz hasta ser menor que el numero, le resta cinco y suma o resta de 1 en 1
def linealBot3(_, maxNum):
    num = random.randint(1, maxNum)
    intentos = 1
    val = 1
    restar = False
    while num != val:
        if val < num:
            if val == 1:
                val = 10
            else:
                val += 10
        elif val > num:
            if restar == False:
                restar = True
                val -= 5
            elif val < num:
                val += 1
            else:
                val -= 1
        intentos += 1
    return intentos