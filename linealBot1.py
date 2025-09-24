import random
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