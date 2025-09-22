import algoritmoBot1
import randomBot1
import randomBot2
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
        bot_en_uso = int(input("Which bot do you want to use?  "
            "\n 1. Algoritmic bot \n 2. Random bot 1(repeat numbers)\n 3. Random bot 2(doesn't repeat numbers) \n Select the number: "))
        if bot_en_uso == 1 or bot_en_uso == 2 or bot_en_uso == 3: break
        else: print("Invalid input.")

    n_cores = os.cpu_count() - 1

    if bot_en_uso == 1:
        func = partial(algoritmoBot1.algoritmo_bot, maxNum=maxNum)
        with Pool(processes=n_cores) as p:
            resultados = p.map(func, range(num_juegos))

        media_intentos = sum(resultados) / num_juegos
        print(f"Algoritmic bot in {num_juegos} games averaged {media_intentos} tries to find a number between 1 and {maxNum}")

    elif bot_en_uso == 2:
        func = partial(randomBot1.random_bot1, maxNum=maxNum)
        with Pool(processes=n_cores) as p:
            resultados = p.map(func, range(num_juegos))

        media_intentos = sum(resultados) / num_juegos
        print(f"Random bot 1 in {num_juegos} games averaged {media_intentos} tries to find a number between 1 and {maxNum}")

    else:
        func = partial(randomBot2.random_bot2, maxNum=maxNum)
        with Pool(processes=n_cores) as p:
            resultados = p.map(func, range(num_juegos))

        media_intentos = sum(resultados) / num_juegos
        print(f"Random bot 2 in {num_juegos} games averaged {media_intentos} tries to find a number between 1 and {maxNum}")