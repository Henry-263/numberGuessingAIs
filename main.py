import random
import os
from multiprocessing import Pool

#Juego donde se comprueba el numero
def juego(_):
    global maxNum, bot_en_uso
    num = random.randint(1,maxNum)
    intentos = 1

    if bot_en_uso == "aleatorio":
        while num != random_bot():
            intentos += 1
    elif bot_en_uso == "algoritmo":
        intentos = algoritmo_bot(num,intentos)

    return intentos

#Bot aleatorio, solo devuelve un numero aleatorio
def random_bot():
    val = random.randint(1,maxNum)
    return val

#Bot algoritmo, divide en mitad las posibilidades segun si es mayor o menor
def algoritmo_bot(num, intentos):
    val = maxNum / 2
    max, min = maxNum + 1, 0
    mayor = True

    while num != val:
        if val > num:
            mayor = False
        else:
            mayor = True
        if mayor:
            min = val
        else:
            max = val
        val = (max + min) // 2
        intentos += 1
    return intentos

def init_pool(maxNum_, bot_en_uso_):
    global maxNum, bot_en_uso
    maxNum = maxNum_
    bot_en_uso = bot_en_uso_
#Inicio programa

if __name__ == "__main__":

    num_juegos = 1000000
    maxNum = 100
    bot_en_uso = "aleatorio"

    n_cores = os.cpu_count() - 1

    with Pool(processes=n_cores, initializer=init_pool, initargs=(maxNum, bot_en_uso)) as p:
        resultados = p.map(juego, range(num_juegos))

    media_intentos = sum(resultados) / num_juegos
    print(f"El bot {bot_en_uso} ha tardado en {num_juegos} juegos una media de {media_intentos} intentos")