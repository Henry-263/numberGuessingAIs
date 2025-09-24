import botsFunc
import os
from multiprocessing import Pool
from functools import partial

#Inicio programa

if __name__ == "__main__":

    bots = {
        1: ("Algoritmic bot A", botsFunc.algoritmo_bot, "(Tries the number between the range of possible numbers)"),
        2: ("Random bot A", botsFunc.random_bot1, "(Chooses a random number)"),
        3: ("Random bot B", botsFunc.random_bot2, "(Chooses a random number, but without repeating a number)"),
        4: ("Lineal bot A", botsFunc.linealBot1, "(Tries every number starting in 1: 1-2-3-4-5...)")
    }

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
        print("Bots:")
        for i in range(len(bots)):
            print(f"{i+1}. {bots[i + 1][0]} {bots[i + 1][2]}")
        bot_en_uso = int(input("Which bot do you want to use:  "))
        if bot_en_uso in bots: break
        else: print("Invalid input.")

    n_cores = os.cpu_count() - 1

    botName, funcName = bots[bot_en_uso][0], bots[bot_en_uso][1]
    func = partial(funcName, maxNum=maxNum)
    with Pool(processes=n_cores) as p:
        resultados = p.map(func, range(num_juegos))

    media_intentos = sum(resultados) / num_juegos
    print(f"{botName} in {num_juegos} games averaged {round(media_intentos, 3)} tries to find a number between 1 and {maxNum}")