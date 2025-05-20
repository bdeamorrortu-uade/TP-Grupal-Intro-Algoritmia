import random


top_5_scores = [{ "player": "11111111", "attempts": 1}, { "player": "22222222", "attempts": 4}, { "player": "33333333", "attempts": 5}, { "player": "44444444", "attempts": 10000}, { "player": "55555555", "attempts": 10000000}]

game_instructions = """
Bienvenido a "..."!

El juego consiste en adivinar un número de 4 cifras en el menor número de intentos posible.

Para cada intento, se te dará una pista: Si es mayor o menor al número a adivinar.

Para ganar, debes adivinar el número en el menor número de intentos posible.

Para salir, ingresa "-1" como número.

Comencemos!

"""

# Funcion reutilizable para pedir número al usuario
def ask_for_number():
    user_number = int(input("Ingrese un número de 4 cifras: "))
    return user_number

# Funcion que se encarga de comparar puntaje del usuario con los top 5 e ingresarlo en caso de ser necesario
def handle_correct_guess(attempts):
    print("¡Felicidades! Has adivinado el número.")

    # Si la cant. de intentos del usuario es menor al último del top 5, se agrega a la lista
    if(top_5_scores[len(top_5_scores) - 1]["attempts"] > attempts):
        print("¡Te encuentras en el top 5 de mejores puntajes!")
        identification = input("Ingrese su identificación para guardar el resultado: ")

        # Se agrega el intento a la lista - pasa a tener 6 elementos
        top_5_scores.append({ "player": identification, "attempts": attempts })

        # Se ordena la lista de menor a mayor intentos
        top_5_scores.sort(key=lambda x: x["attempts"])

        # Se elimina el último intento de la lista - vuelve a tener 5 elementos
        top_5_scores.pop(5)

# Funcion encargada de realizar bucle hasta que el usuario adivine o decida salir del juego
def ask_and_check_number(random_number):
    attempts = 0

    user_number = ask_for_number()

    while(user_number != -1 and user_number != random_number):
        if(user_number < 1000 or user_number > 9999):
            # Como el valor es incorrecto, se vuelve a pedir un número y no se cuenta como intento
            user_number = int(input("El número ingresado no es de 4 cifras. Vuelva a ingresar un número: "))
        elif(user_number > random_number):
            attempts += 1
            print("El número a adivinar es MENOR. Vuelva a intentarlo")
            user_number = ask_for_number()
        else:
            attempts += 1
            print("El número a adivinar es MAYOR. Vuelva a intentarlo")
            user_number = ask_for_number()

    # Si el bucle terminó por adivinar el número
    if(user_number == random_number):
        # Se agrega el intento
        attempts += 1
        # Se checkea si el puntaje es top 5
        handle_correct_guess(attempts)

    return attempts

# Funcion encargada de preguntar al usuario si desea volver a jugar
def ask_to_play_again():
    play_again = input("¿Quieres volver a jugar? (si/no): ")

    if(play_again == "si"):
        start_game()
    else:
        print("Gracias por jugar!")

# Funcion central que ejecuta el juego
def start_game():
    print(game_instructions)

    random_number = random.randint(1000, 9999)

    attempts = ask_and_check_number(random_number)

    print("El número a adivinar era: ", random_number)
    print("Cantidad de intentos: ", attempts)
    print("Top 5 scores: ", top_5_scores)
    
    ask_to_play_again()



start_game()

