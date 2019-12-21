import math as m
import numpy as np
import cupy as cp

board = np.zeros((10,10,1))
board = board.astype('int')

def ship_v(ship, i, j):
    s = 0
    if (i <= 9) and (j <= 9) and (i >= 0) and (j >= 0) and ((i+ship) <= 10):
        for a in range(ship):
            s = s + board[i + a, j, 0]
        if s == 0:
            for b in range(10):
                for c in range(10):
                    if board[b, c, 0] == ship:
                        s = s + 1
                    else:
                        pass
            if s == 0 or s == 3:
                for d in range(ship):
                    board[i + d, j, 0] = ship
            else:
                pass
                #print("Ship repeat")
        else:
            pass
            #print("Ship overlap")
    else:
        pass
        #print("Bad index")

    if s == 0 or s == 3:
        return(0)
    else:
        return(1)

def ship_h(ship, i, j):
    s = 0
    if (i <= 9) and (j <= 9) and (i >= 0) and (j >= 0) and ((j+ship) <= 10):
        for a in range(ship):
            s = s + board[i, j+a, 0]
        if s == 0:
            for b in range(10):
                for c in range(10):
                    if board[b, c, 0] == ship:
                        s = s + 1
                    else:
                        pass
            if s == 0 or s == 3:
                for d in range(ship):
                    board[i, j + d, 0] = ship
            else:
                pass
                #print("Ship repeat")
        else:
            pass
            #print("Ship overlap")
    else:
        pass
        #print("Bad index")
    if s == 0 or s == 3:
        return(0)
    else:
        return(1)

def board_clear():
    for i in range(10):
        for j in range(10):
            board[i, j, 0] = 0

def final_check():
    s = 0
    for i in range(10):
        for j in range(10):
            s = s + board[i, j, 0]
    if s == 63:
        return(0)
    else:
        return(1)

def generate_boards(c1, c2, c3, c4, c5, c_file):
    loop_s = 0
    if c1 == 0:
        if c2 == 0:
            if c3 == 0:
                if c4 == 0:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for ij in range(10):
                                                            for i2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_h(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                else:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for j_3 in range(10):
                                                    for i_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_h(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for j_3 in range(10):
                                                    for i_3 in range(8):
                                                        for j2 in range(10):
                                                            for i2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_h(3, i_3, j_3)
                                                                c2 = ship_h(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
            else:
                if c4 == 0:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for j3 in range(10):
                                            for i3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_h(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()

                    else:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for j3 in range(10):
                                            for i3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for j2 in range(10):
                                                            for i2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_h(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_h(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                else:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for j3 in range(10):
                                            for i3 in range(8):
                                                for j_3 in range(10):
                                                    for i_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_h(3, i3, j3)
                                                                c_3 = ship_h(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
        else:
            if c3 == 0:
                if c4 == 0:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for j4 in range(10):
                                    for i4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_h(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        for i5 in range(10):
                            for j5 in range(6):
                                for j4 in range(10):
                                    for i4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for j2 in range(10):
                                                            for i2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_h(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_h(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()

                else:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for j4 in range(10):
                                    for i4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for j_3 in range(10):
                                                    for i_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_h(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_h(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
            else:
                if c4 == 0:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for j3 in range(10):
                                            for i3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_h(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
                else:
                    if c5 == 0:
                        for i5 in range(10):
                            for j5 in range(6):
                                for j4 in range(10):
                                    for i4 in range(7):
                                        for j3 in range(10):
                                            for i3 in range(8):
                                                for j_3 in range(10):
                                                    for i_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_v(5, i5, j5)
                                                                c4 = ship_h(4, i4, j4)
                                                                c3 = ship_h(3, i3, j3)
                                                                c_3 = ship_h(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
    else:
        if c2 == 0:
            if c3 == 0:
                if c4 == 0:
                    if c5 == 0:
                        for j5 in range(10):
                            for i5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_h(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        for j5 in range(10):
                            for i5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for j2 in range(10):
                                                            for i2 in range(9):
                                                                c5 = ship_h(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_h(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                else:
                    if c5 == 0:
                        for j5 in range(10):
                            for i5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for j_3 in range(10):
                                                    for i_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_h(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_h(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
            else:
                if c4 == 0:
                    if c5 == 0:
                        for j5 in range(10):
                            for i5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for j3 in range(10):
                                            for i3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_h(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_h(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
                else:
                    if c5 == 0:
                        pass
                    else:
                        pass
        else:
            if c3 == 0:
                if c4 == 0:
                    if c5 == 0:
                        for j5 in range(10):
                            for i5 in range(6):
                                for j4 in range(10):
                                    for i4 in range(7):
                                        for i3 in range(10):
                                            for j3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_h(5, i5, j5)
                                                                c4 = ship_h(4, i4, j4)
                                                                c3 = ship_v(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
                else:
                    if c5 == 0:
                        pass
                    else:
                        pass
            else:
                if c4 == 0:
                    if c5 == 0:
                        for j5 in range(10):
                            for i5 in range(6):
                                for i4 in range(10):
                                    for j4 in range(7):
                                        for j3 in range(10):
                                            for i3 in range(8):
                                                for i_3 in range(10):
                                                    for j_3 in range(8):
                                                        for i2 in range(10):
                                                            for j2 in range(9):
                                                                c5 = ship_h(5, i5, j5)
                                                                c4 = ship_v(4, i4, j4)
                                                                c3 = ship_h(3, i3, j3)
                                                                c_3 = ship_v(3, i_3, j_3)
                                                                c2 = ship_v(2, i2, j2)
                                                                cf = final_check()

                                                                if (c5 + c4 + c3 + c_3 + c2 + cf) == 0:
                                                                    board_t = np.transpose(board, (1,0,2))
                                                                    if loop_s == 0:
                                                                        loop_s = 1
                                                                        board_w = board
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                    elif board_w.shape[2] == 5000:
                                                                        name = "board_list_" + str(c_file)
                                                                        outfile = open("%s.npy" % name, "wb")
                                                                        np.save(outfile, board_w)
                                                                        print("Just wrote " + str(c_file*5000) + " boards to file.")
                                                                        print(str(i5) + " " +str(j5))
                                                                        print(str(i4) + " " +str(j4))
                                                                        print(str(i3) + " " +str(j3))
                                                                        print(str(i_3) + " " +str(j_3))
                                                                        print(str(i2) + " " +str(j2))
                                                                        outfile.close()
                                                                        c_file = c_file + 1
                                                                        loop_s = 0
                                                                    else:
                                                                        board_w = np.concatenate((board_w, board), axis=2)
                                                                        board_w = np.concatenate((board_w, board_t), axis=2)
                                                                        board_clear()
                                                                else:
                                                                    board_clear()
                    else:
                        pass
                else:
                    if c5 == 0:
                        pass
                    else:
                        pass
    return(c_file)

def find_boards():
    c_file = 0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        print(a, b, c, d, e)
                        c_file = generate_boards(a, b, c, d, e, c_file)

find_boards()
