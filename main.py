import random

global maxNum
#Juego donde se comprueba el numero
def juego(numero_bot, bot_en_uso):
    num = random.randint(1,maxNum)
    intentos = 1

    if bot_en_uso == "aleatorio":
        while num != random_bot():
            intentos += 1
    elif bot_en_uso == "algoritmo":
        intentos = algoritmo_bot(num,intentos)

    return intentos

#Bot random, solo devuelve un numero aleatorio
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

#Inicio programa
maxNum = 100
media_intentos = 0
num_juegos = 100000

for i in range(num_juegos):
    media_intentos += juego(i, "algoritmo")

media_intentos = media_intentos / num_juegos

print(f"El bot algoritmo a tardado en {num_juegos} juegos una media de {media_intentos} intentos")

media_intentos = 0

for i in range(num_juegos):
    media_intentos += juego(i, "aleatorio")

media_intentos = media_intentos / num_juegos

print(f"El bot aleatorio a tardado en {num_juegos} juegos una media de {media_intentos} intentos")