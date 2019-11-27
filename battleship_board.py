import math as m
import numpy as np
#import cupy as cp
from random import randint
import pickle

board = np.zeros((10,10))
board = board.astype('int')

global control

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

def board_erase():
    board = np.zeros((10,10))
    board = board.astype('int')

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

def ship_h(ship, i, j):
    control = 0
    double_ship_check(ship)

    if (i <= 9) and (j <= 9) and (i >= 0) and (j >= 0) and (control == 0):
        for a in range(ship+1):
            if board[i, j+a] == 0 and (control == 0):
                board[i, j+a] = ship
            else:
                control = 1
                print("Bad index", i, j)
                break
    else:
        control = 1
        print("Bad index", i, j, control)
def save():
    np.save('file.npy', board)

def load():
    board = np.load('file.npy')

def board_creator():
    ship_v(5, 4, 9)
    ship_h(4, 0, 1)
    save()
    board_erase()
    print(board)


board_creator()
