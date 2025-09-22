import random
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