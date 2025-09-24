#Bot random1, devuelve numero aleatorio(se repiten numeros)
import random
def random_bot1(_,maxNum):
    intentos = 0
    num = random.randint(1, maxNum)
    val = 0
    while num != val:
        val = random.randint(1, maxNum)
        intentos += 1
    return intentos