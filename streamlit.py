import random
import streamlit as st
from algorithms import insert_and_sort_top_scores

# Variables de st
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1000, 9999)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'show_save_score' not in st.session_state:
    st.session_state.show_save_score = False
if 'show_results_dialog' not in st.session_state:
    st.session_state.show_results_dialog = False
if 'top_5_scores' not in st.session_state:
    st.session_state.top_5_scores = [
        ["11111111", 1],
        ["22222222", 4],
        ["33333333", 5],
        ["44444444", 10000],
        ["55555555", 10000000]
    ]

def reset_game():
    st.session_state.random_number = random.randint(1000, 9999)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.show_save_score = False
    st.session_state.identification = ""
    st.session_state.show_results_dialog = False

def finish_game(exit=False):
    st.session_state.show_save_score =  (not exit) and (st.session_state.top_5_scores[-1][1] > st.session_state.attempts)
    st.session_state.game_over = True
    st.session_state.show_results_dialog = True

def save_score(identification):
    new_score = [identification, st.session_state.attempts]
    new_top_scores = insert_and_sort_top_scores(st.session_state.top_5_scores, new_score)
    st.session_state.top_5_scores = new_top_scores
    st.session_state.show_save_score = False

def validate_identification(identification):
    return identification.isdigit() and len(identification) >= 5

# Contenido del juego
st.title("🎯 Adivina el número")
st.write("""
Bienvenido a "Adivina el número"!

El juego consiste en adivinar un número de 4 cifras en el menor número de intentos posible.
Para cada intento, se te dará una pista: si el número es mayor o menor al número a adivinar.
Ingresa -1 para salir del juego.
""")

st.subheader("🏆 Top 5 Puntajes")
for score in st.session_state.top_5_scores:
    st.write(f"Jugador: {score[0]}, Intentos: {score[1]}")

# Mostrar input solo si el juego no terminó y el diálogo no está abierto
if not st.session_state.game_over and not st.session_state.show_results_dialog:
    guess = st.text_input("Ingrese un número de 4 cifras:", key="guess_input")
    guess_button = st.button("Intentar")

    if guess_button:
        if guess == "-1":
            finish_game(True)
        elif guess.isdigit() and len(guess) == 4:
            user_number = int(guess)
            st.session_state.attempts += 1
            if user_number == st.session_state.random_number:
                finish_game()
            elif user_number > st.session_state.random_number:
                st.session_state.message = "El número a adivinar es MENOR. Vuelva a intentarlo."
            else:
                st.session_state.message = "El número a adivinar es MAYOR. Vuelva a intentarlo."
        else:
            st.session_state.message = "Entrada inválida. Debe ingresar un número entero de 4 cifras."

    if st.session_state.message:
        st.info(st.session_state.message)

# Modal
@st.dialog("Resultados del juego")
def show_results_dialog():
    st.write(f"El número a adivinar era: {st.session_state.random_number}")
    st.write(f"Cantidad de intentos: {st.session_state.attempts}")
    valid = True
    identification = None
    if st.session_state.show_save_score:
        st.success("¡Te encuentras en el top 5 de mejores puntajes!")
        identification = st.text_input("Ingrese su identificación para guardar el resultado:", key="identification_input")
        valid = validate_identification(identification)
        if (not valid) and identification:
            st.error("Entrada inválida. Ingrese un valor numérico correspondiente a su identificacion de al menos 5 dígitos.")
    finalizar_btn = st.button("Finalizar", key="finalizar_btn", disabled=(st.session_state.show_save_score and not valid))
    if finalizar_btn:
        if st.session_state.show_save_score and valid:
            save_score(identification)
        reset_game()
        st.rerun()

# Mostrar modal al finalizar el juego
if st.session_state.game_over and st.session_state.show_results_dialog:
    show_results_dialog()
