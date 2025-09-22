#Bot algoritmo, divide en mitad las posibilidades segun si es mayor o menor
import random
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