import botsFunc
import os
from multiprocessing import Pool
from functools import partial

#Inicio programa

if __name__ == "__main__":

    #Guardamos todos los bots con su nombre, localizacion y como funciona
    bots = {
        0: ("All bots", "", "(Executes all bots)"),
        1: ("Algoritmic bot A", botsFunc.algoritmo_bot, "(Tries the number between the range of possible numbers)"),
        2: ("Random bot A", botsFunc.random_bot1, "(Chooses a random number)"),
        3: ("Random bot B", botsFunc.random_bot2, "(Chooses a random number, but without repeating a number)"),
        4: ("Lineal bot A", botsFunc.linealBot1, "(Tries every number starting in 1: 1-2-3-4-5...)"),
        5: ("Lineal bot B", botsFunc.linealBot2, "(Checks pairs of numbers from the outside in: first 1 and 100, then 2 and 99, then 3 and 98, etc., until it finds the target number)")
    }


    # Preguntamos y guardamos los datos maxNum, num_juegos y el tipo de bot introducidos por el usuario
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
            print(f"{i}. {bots[i][0]} {bots[i][2]}")
        bot_en_uso = int(input("Which bot do you want to use:  "))
        if bot_en_uso in bots: break
        else: print("Invalid input.")


    #Utilizando la maxima capacidad de nucleos posible
    if os.cpu_count() > 1:
        n_cores = os.cpu_count() - 1
    else:
        n_cores = os.cpu_count()

    #Ejecutamos la funcion del bot correspondiente
    botName, funcName = bots[bot_en_uso][0], bots[bot_en_uso][1]
    if bot_en_uso != 0:
        func = partial(funcName, maxNum=maxNum)
        with Pool(processes=n_cores) as p:
            resultados = p.map(func, range(num_juegos))

        media_intentos = sum(resultados) / num_juegos
        print(f"{botName} in {num_juegos} games averaged {round(media_intentos, 3)} tries to find a number between 1 and {maxNum}")
    else:
        for i in range(1, len(bots)):
            botName, funcName = bots[i][0], bots[i][1]

            func = partial(funcName, maxNum=maxNum)
            with Pool(processes=n_cores) as p:
                resultados = p.map(func, range(num_juegos))

            media_intentos = sum(resultados) / num_juegos
            print(f"{i}. {botName} in {num_juegos} games averaged {round(media_intentos, 3)} tries to find a number between 1 and {maxNum}")