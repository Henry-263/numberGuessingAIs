import algoritmoBot1
import randomBot1
import os
from multiprocessing import Pool
from functools import partial
#Inicio programa

if __name__ == "__main__":

    bot_en_uso = "algoritmo"
    print("Program to compare bots trying to find a random number.")
    while True:
        maxNum = int(input("The number to find is between 1 and... "))
        if maxNum > 0: break
        else: print("The number is not valid.")
    while True:
        num_juegos = int(input("How many games is the bot going to play:  "))
        if num_juegos > 0: break
        else: print("The number is not valid.")
    while True:
        bot_en_uso = int(input("Which bot do you want to use?  \n 1.Algoritmic bot \n 2. Random bot \n Select the number: "))
        if bot_en_uso == 1 or bot_en_uso == 2: break
        else: print("Invalid input.")

    n_cores = os.cpu_count() - 1

    if bot_en_uso == 1:
        func = partial(algoritmoBot1.algoritmo_bot, maxNum=maxNum)
        with Pool(processes=n_cores) as p:
            resultados = p.map(func, range(num_juegos))

        media_intentos = sum(resultados) / num_juegos
        print(f"El bot algoritmo ha tardado en {num_juegos} juegos una media de {media_intentos} intentos en adivinar un numero del 1 al {maxNum}")
    else:
        func = partial(randomBot1.random_bot1, maxNum=maxNum)
        with Pool(processes=n_cores) as p:
            resultados = p.map(func, range(num_juegos))

        media_intentos = sum(resultados) / num_juegos
        print(f"El bot aleatorio 1 ha tardado en {num_juegos} juegos una media de {media_intentos} intentos en adivinar un numero del 1 al {maxNum}")
