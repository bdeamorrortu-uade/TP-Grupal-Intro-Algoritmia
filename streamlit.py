import random
import streamlit as st


top_5_scores = [{ "player": "11111111", "attempts": 1}, { "player": "22222222", "attempts": 4}, { "player": "33333333", "attempts": 5}, { "player": "44444444", "attempts": 10000}, { "player": "55555555", "attempts": 10000000}]

st.title("🎯 Adivina el número")
st.write("""
Bienvenido a "Adivina el número"!

El juego consiste en adivinar un número de 4 cifras en el menor número de intentos posible.

Para cada intento, se te dará una pista: si el número es mayor o menor al número a adivinar.

Ingresa -1 para salir del juego.
""")

# Funcion reutilizable para pedir número al usuario
def ask_for_number():
    user_number = int(st.text_input("Ingrese un número de 4 cifras: "))
    return user_number

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



# Funcion que se encarga de comparar puntaje del usuario con los top 5 e ingresarlo en caso de ser necesario
def handle_correct_guess(attempts):
    st.write("¡Felicidades! Has adivinado el número.")

    # Si la cant. de intentos del usuario es menor al último del top 5, se agrega a la lista
    if(top_5_scores[len(top_5_scores) - 1]["attempts"] > attempts):
        st.write("¡Te encuentras en el top 5 de mejores puntajes!")
        identification = st.text_input("Ingrese su identificación para guardar el resultado: ")

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
        if(user_number > random_number):
            st.write("El número a adivinar es MENOR. Vuelva a intentarlo")
        else:
            st.write("El número a adivinar es MAYOR. Vuelva a intentarlo")
        attempts += 1
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
    play_again = st.text_input("¿Quieres volver a jugar? (si/no): ")

    if(play_again == "si"):
        start_game()
    else:
        st.write("Gracias por jugar!")

# Funcion central que ejecuta el juego
def start_game():

    random_number = random.randint(1000, 9999)

    attempts = ask_and_check_number(random_number)

    st.write("El número a adivinar era: ", random_number)
    st.write("Cantidad de intentos: ", attempts)
    st.write("Top 5 scores: ", top_5_scores)
    
    ask_to_play_again()



start_game()

