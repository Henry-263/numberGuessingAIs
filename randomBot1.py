#Bot algoritmo, divide en mitad las posibilidades segun si es mayor o menor
import random
def random_bot1(_,maxNum):
    intentos = 0
    num = random.randint(1, maxNum)
    val = 0
    while num != val:
        val = random.randint(1, maxNum)
        intentos += 1
    return intentos