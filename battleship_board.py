import math as m
import numpy as np
import cupy as cp
from random import randint

board = np.zeros((10,10))
board = board.astype('int')
global control
global c_3
global h_c
global v_c



def double_ship_check(ship):
    c_3 = 0
    control= 0
    if ship != 3:
        for i in range(10):
            for j in range(10):
                if board[i,j] == ship:
                    control = 1
    else:
        for i in range(10):
            for j in range(10):
                if board[i,j] == ship:
                    c_3 = c_3 + 1
        if c_3 == 3 or c_3 == 0:
            pass
        else:
            control = 1
    c_3 = 0

def ship_v(ship, i, j):
    control = 0
    double_ship_check(ship)

    if (i <= 9) and (j <= 9) and (i >= 0) and (j >= 0) and (control == 0):
        for a in range(ship+1):
            if board[i + a, j] == 0 and (control == 0):
                board[i + a, j] = ship
            else:
                control = 1
                print("Bad index", i, j)
                break
    else:
        control = 1
        print("Bad index", i, j, control)

    v_c = v_c + 1

def board_creator():
    global v_c
    global h_c
    v_c = 0
    h_c = 0
    ship_v(5, 0, 0)
    ship_v(4, 0, 1)

    print(board)

board_creator()
