import math as m
import numpy as np
import cupy as cp
from random import randint
from tqdm import tqdm

board = np.zeros((10,10))
board = board.astype('int')

def ship_v(ship, i, j):
    control = 0
    double_ship_check(ship)

    if (i <= 9) and (j <= 9) and (i >= 0) and (j >= 0) and (control == 0) and ((i+ship) <= 9):
        for a in range(ship):
            if board[i + a, j] == 0 and (control == 0):
                board[i + a, j] = ship
            else:
                control = 1
                #print("Bad index", i, j)
                break
    else:
        control = 1
        #print("Bad in

def ship_h(ship, i, j):
    control = 0

    if (i <= 9) and (j <= 9) and (i >= 0) and (j >= 0) and (control == 0) and ((j+ship) <= 9):
        for a in range(ship):
            if board[i, j + a] == 0 and (control == 0):
                board[i, j + a] = ship
            else:
                control = 1
                #print("Bad index", i, j)
                break
    else:
        control = 1
        #print("Bad index", i, j, control)

def final_board_check():
    global f_c
    f_c = 0
    for i in range(10):
        for j in range(10):
            if board[i, j] != 0:
                f_c = f_c + 1
            else:
                pass

def boards():
    i_5 = 0
    i_4 = 0
    i_3 = 0
    i3 = 0
    i_2 = 0

    j_5 = 0
    j_4 = 0
    j_3 = 0
    j3 = 0
    j_2 = 0

    for i_5 in range(10):
        for j_5 in range(10):

            for i_4 in range(10):
                for j_4 in range(10):


                    for i_3 in range(10):
                        for j_3 in range(10):

                            for i3 in range(10):
                                for j3 in range(10):

                                    for i_2 in range(10):
                                        for j_2 in range(10):
                                            ship_v(5, i_5, j_5)
                                            ship_v(4, i_4, j_4)
                                            ship_v(3, i_3, j_3)
                                            ship_v(3, i3, j3)
                                            ship_v(2, i_2, j_2)
                                            print(board)
                                            #print(np.transpose(board))
                                            #print(i_5, j_5)
                                            #print(i_4, j_4)
                                            #print(i_3, j_3)
                                            #print(i3, j3)
                                            #print(i_2, j_2)



boards()
