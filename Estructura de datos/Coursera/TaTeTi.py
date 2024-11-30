# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:49:51 2021

@author: MedNov
"""

Tablero = [
    "_", "_", "_",  
    "_", "_", "_",  
    "_", "_", "_"]  

    # [0] [1] [2]
    # [3] [4] [5]
    # [6] [7] [8]



game_still_going = True
winner = None
current_player = "X"

#Gato
def display_board():
    print(" -------")
    print(" | Gato |")
    print(" -------")
    print(" |" + Tablero[0] + "|" + Tablero[1] + "|" + Tablero[2] + "|")
    print(" |" + Tablero[3] + "|" + Tablero[4] + "|" + Tablero[5] + "|")
    print(" |" + Tablero[6] + "|" + Tablero[7] + "|" + Tablero[8] + "|")

def play_game():
    #JuegoEnCurso
    display_board()

    while game_still_going:        
        # Maneja el turno del jugador  
        handle_turn(current_player)
        
        check_if_game_over()
        #CambioDeJugador
        flip_player()
        
    if winner == "X" or winner == "O":
        print(winner + " ha ganado.")
    elif winner == None:
        print("Fue un empate.")


# Turno de los jugadores
def handle_turn(player):
    print("Tu eres " + player)
    
    position = input("Escoje una posicion entre el 1 y el 9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Escoje una posicion entre el 1 y el 9: ")
        position = int(position) - 1

        if Tablero[position] == "_":
            valid = True
        else:
            print("El lugar ya esta ocupado")


    Tablero[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():

    global game_still_going
    row_1 = Tablero[0] == Tablero[1] == Tablero[2] != "_"
    row_2 = Tablero[3] == Tablero[4] == Tablero[5] != "_"
    row_3 = Tablero[6] == Tablero[7] == Tablero[8] != "_"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return Tablero[0]
    if row_2:
        return Tablero[3]
    if row_3:
        return Tablero[6]
    return


def check_columns():  

    global game_still_going
    column_1 = Tablero[0] == Tablero[3] == Tablero[6] != "_"
    column_2 = Tablero[1] == Tablero[4] == Tablero[7] != "_"
    column_3 = Tablero[2] == Tablero[5] == Tablero[8] != "_"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return Tablero[0]
    if column_2:
        return Tablero[1]
    if column_3:
        return Tablero[2]
    return


def check_diagonals():  
    
    global game_still_going
    diagonal_1 = Tablero[0] == Tablero[4] == Tablero[8] != "_"
    diagonal_2 = Tablero[6] == Tablero[4] == Tablero[2] != "_"


    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return Tablero[0]
    if diagonal_2:
        return Tablero[6]
    return


def check_if_tie():
    global game_still_going
    if "_" not in Tablero:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()