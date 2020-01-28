import random
import numpy as np
import sys


def generate_board():
    # Utilizamos la libreria de numpy para generar una matrix 3x3, con valores [0,2]
    columns = 3
    rows = 3
    # Los ceros en el array representan espacios vacios,
    # Los números 1 representan los zeros.
    # Los números 2 representan las equiz.
    arr = np.random.randint(3, size=(rows, columns))
    #arr = [[2, 2, 1], [0, 1, 1], [1, 2, 2]]
    return arr


def check_rows(board):
    for row in board:
        newset = set(row)
        if (len(newset) == 1):
            if(newset != {0}):
                return newset

def check_columns(board):
    board = np.transpose(board)
    for row in board:
        newset = set(row)
        if (len(newset) == 1):
            if(newset != {0}):
                return newset

def check_diagonals(board):
    if(board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
        return 1
    if(board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
        return 2
    if(board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
        return 1
    if(board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2):
        return 2


def get_winner(board, zs, xs):
    if (check_rows(board) == {1} or check_columns(board) == {1}):
        if(zs == 3 and xs == 3):
            sys.exit('Juego invalido, no puede haber dos ganadores.')
        sys.exit('El ganador es o.')
    elif (check_rows(board) == {2} or check_columns(board) == {2}):
        if(zs == 3 and xs == 3):
            sys.exit('Juego invalido, no puede haber dos ganadores.')
        sys.exit('El ganador es x.')
    elif(check_diagonals(board) == 1):
        sys.exit('El ganador es o.')
    elif(check_diagonals(board) == 2):
        sys.exit('El ganador es x.')


# La variable 'zs' guarda la cantidad de zeros.
# La variable 'zs' guarda la cantidad de zeros.
# La variable 'xs' guarda la cantidad de equiz.
zs, xs = 0, 0

# Se genera un juego aleatorio
board = generate_board()

translated_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

for x in range(3):
    for k in range(3):
        if(board[x][k] == 1):
            zs += 1
            translated_board[x][k] = 'o'
        elif(board[x][k] == 2):
            xs += 1
            translated_board[x][k] = 'x'

for x in range(3):
    print(translated_board[x])

if (zs == 4 and xs == 5):
    sys.exit('Empate')
elif (zs == 5 and xs == 4):
    sys.exit('Empate')
elif(zs > 4 or xs > 4):
    sys.exit('Juego invalido, hay un exceso de jugadas.')
elif (zs == 0 and xs == 0):
    sys.exit('Juego invalido, no hay jugadas.')
elif(max(zs, xs) - min(zs, xs) > 1):
    sys.exit('Juego invalido, el numero de jugadas no corresponde.')

get_winner(board, zs, xs)

sys.exit('Juego invalido.')