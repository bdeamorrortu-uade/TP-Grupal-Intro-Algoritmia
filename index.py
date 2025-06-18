from algorithms import *
import random

# [player_id, attempts]
top_5_scores = [
    ["11111111", 1],
    ["22222222", 4],
    ["33333333", 5],
    ["44444444", 10000],
    ["55555555", 10000000]
]

game_instructions = """
Bienvenido a "..."!

El juego consiste en adivinar un número de 4 cifras en el menor número de intentos posible.

Para cada intento, se te dará una pista: Si es mayor o menor al número a adivinar.

Para ganar, debes adivinar el número en el menor número de intentos posible.

Para salir, ingresa "-1" como número.

Comencemos!
"""

def ask_for_number():
    is_valid = False

    while not is_valid:
        user_input = input("Ingrese un número entero de 4 cifras: ")

        if user_input == "-1":
            return -1

        if user_input.isdigit() and len(user_input) == 4:
            user_number = int(user_input)
            is_valid = True
        else:
            print("Entrada inválida. Debe ingresar un número entero de 4 cifras.")

    return user_number

def handle_correct_guess(attempts):
    print("¡Felicidades! Has adivinado el número.")
    # Se debe declarar top_5_scores como global para que python entienda que no se debe modificar solo localmente
    global top_5_scores 
    if top_5_scores[4][1] > attempts:
        print("¡Te encuentras en el top 5 de mejores puntajes!")
        identification = input("Ingrese su identificación para guardar el resultado: ")
        new_score = [identification, attempts]
        top_5_scores = insert_and_sort_top_scores(top_5_scores, new_score)

def ask_and_check_number(random_number):
    attempts = 0
    user_number = ask_for_number()
    while user_number != -1 and user_number != random_number:
        if user_number > random_number:
            print("El número a adivinar es MENOR. Vuelva a intentarlo")
        else:
            print("El número a adivinar es MAYOR. Vuelva a intentarlo")
        attempts += 1
        user_number = ask_for_number()
    if user_number == random_number:
        attempts += 1
        handle_correct_guess(attempts)
    return attempts

def ask_to_play_again():
    play_again = input("¿Quieres volver a jugar? (si/no): ")
    if play_again == "si":
        start_game()
    else:
        print("Gracias por jugar!")

def start_game():
    print(game_instructions)
    random_number = random.randint(1000, 9999)
    attempts = ask_and_check_number(random_number)
    print("El número a adivinar era: ", random_number)
    print("Cantidad de intentos: ", attempts)
    print("Top 5 scores:")
    for score in top_5_scores:
        print(f"Jugador: {score[0]}, Intentos: {score[1]}")
    ask_to_play_again()

start_game()
