import math
import Computer,Player
from copy import deepcopy
import time

def Children(tabuleiro, maxTurn):
    children = []

    if maxTurn:

        if Computer.Can_Capture(tabuleiro):
            resultado = Computer.Maior_Captura3([], tabuleiro)

            for move in resultado:
                copia = deepcopy(tabuleiro)
                for step in move:
                    Computer.Move(Computer.transform_pos(step[0][0], step[0][1]),Computer.transform_pos(step[1][0], step[1][1]), copia, False)
                children.append(copia)

        else:
            for i in range(10):
                for j in range(10):
                    if tabuleiro[i][j] == 'p':
                        if i+1 < 10 and j-1 > -1:
                            copia = deepcopy(tabuleiro)
                            moved = Computer.Move(Computer.transform_pos(i, j), Computer.transform_pos(i+1, j-1), copia, False)
                            if moved:
                                children.append(copia)
                        if i+1 < 10 and j+1 < 10:
                            copia = deepcopy(tabuleiro)
                            moved = Computer.Move(Computer.transform_pos(i, j), Computer.transform_pos(i + 1, j + 1), copia,False)
                            if moved:
                                children.append(copia)
                    elif tabuleiro[i][j] == 'P':
                        for k in range(10):
                            for l in range(10):
                                if(tabuleiro[k][l] == ' ' and Computer.Is_Open_Diagonal(i,j,k,l,tabuleiro)):
                                    copia = deepcopy(tabuleiro)
                                    moved = Computer.Move(Computer.transform_pos(i,j),Computer.transform_pos(k,l),copia,False)

                                    if moved:
                                        children.append(copia)

    else:
        if Player.Can_Capture(tabuleiro):
            resultado = Player.Maior_Captura3([], tabuleiro)

            for move in resultado:
                copia = deepcopy(tabuleiro)
                for step in move:
                    Player.Move(Player.transform_pos(step[0][0], step[0][1]),Player.transform_pos(step[1][0], step[1][1]), copia, False)
                children.append(copia)


        else:
            for i in range(10):
                for j in range(10):
                    if tabuleiro[i][j] == 'b':
                        if i-1 > -1 and j - 1 > -1:
                            #--------------------------------------------------------
                            copia = deepcopy(tabuleiro)
                            moved = Player.Move(Player.transform_pos(i, j), Player.transform_pos(i - 1, j - 1),copia, False)
                            if moved:
                                children.append(copia)

                        if i-1 > -1 and j + 1 < 10:
                            copia = deepcopy(tabuleiro)
                            moved = Player.Move(Computer.transform_pos(i, j), Computer.transform_pos(i - 1, j + 1),copia, False)
                            if moved:
                                children.append(copia)

                    elif tabuleiro[i][j] == 'B':
                        for k in range(10):
                            for l in range(10):
                                if (tabuleiro[k][l] == ' ' and Player.Is_Open_Diagonal(i, j, k, l,tabuleiro)):
                                    copia = deepcopy(tabuleiro)
                                    moved = Player.Move(Player.transform_pos(i, j), Player.transform_pos(k, l),copia, False)

                                    if moved:
                                        children.append(copia)


    return children

def minimax_decision(tabuleiro, depth):
    operations = []

    if Computer.Can_Capture(tabuleiro):
        resultado = Computer.Maior_Captura3([], tabuleiro)
        for move in resultado:
            copia = deepcopy(tabuleiro)
            for step in move:
                Computer.Move(Computer.transform_pos(step[0][0], step[0][1]),Computer.transform_pos(step[1][0], step[1][1]), copia, False)
            #operations.append((move,minimax_value(copia,True,depth)))
            operations.append((move, alphabeta_value(copia,depth, -9999,+9999,False)))


    else:
        for i in range(10):
            for j in range(10):
                if tabuleiro[i][j] == 'p':
                    if i + 1 < 10 and j - 1 > -1:
                        copia = deepcopy(tabuleiro)
                        moved = Computer.Move(Computer.transform_pos(i, j), Computer.transform_pos(i + 1, j - 1), copia,False)
                        if moved:
                            operations.append((((i,j),(i+1,j-1)), alphabeta_value(copia, depth, -9999, +9999, False)))
                    if i + 1 < 10 and j + 1 < 10:
                        copia = deepcopy(tabuleiro)
                        moved = Computer.Move(Computer.transform_pos(i, j), Computer.transform_pos(i + 1, j + 1), copia,False)
                        if moved:
                            operations.append((((i,j),(i+1,j+1)), alphabeta_value(copia, depth, -9999, +9999, False)))
                elif tabuleiro[i][j] == 'P':
                    for k in range(10):
                        for l in range(10):
                            if (tabuleiro[k][l] == ' ' and Computer.Is_Open_Diagonal(i, j, k, l,tabuleiro)):
                                copia = deepcopy(tabuleiro)
                                moved = Computer.Move(Computer.transform_pos(i, j), Computer.transform_pos(k, l), copia,False)
                                if moved:
                                    operations.append((((i,j),(k,l)), alphabeta_value(copia, depth, -9999, +9999, False)))


    value = -99999
    best_op = ()
    for op in operations:
        if op[1]> value:
            value = op[1]
            best_op = op[0]

    print(operations)
    return best_op


def alphabeta_value(tabuleiro,depth,alpha,beta,maxTurn):
    if depth == 0:
        return heuristic2(tabuleiro)
    children = Children(tabuleiro, maxTurn)

    if maxTurn:
        value = -9999
        for child in children:
            value = max(value, alphabeta_value(child,depth-1,alpha,beta,False))
            alpha = max(alpha,value)

            if alpha >= beta:    # B cut-off
                break


        return value

    else:
        value = 9999
        for child in children:
            value = min(value, alphabeta_value(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:    # A cut-off
                break

        return value


def heuristic(board):
    p = 0
    b = 0

    for line in board:
        p += line.count('p') + line.count('P')*2
        b += line.count('b') + line.count('B') * 2

    return p - b


def heuristic2(board):
    p = 0
    b = 0

    count = 1
    for line in board:
        if count >= 5:
            p += line.count('p')*7 + line.count('P') * 10
            b += line.count('b')*5 + line.count('B') * 10

        else:
            p += line.count('p')*5 + line.count('P')*10
            b += line.count('b')*7 + line.count('B') * 10
        count += 1

    return p - b