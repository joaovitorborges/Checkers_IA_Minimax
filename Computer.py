import string
from copy import deepcopy
import Minimax

# from anytree import Node, RenderTree

def read_pos(pos):  # read inputs such as "9c" or "10d" and return them as coordinates

    if (len(pos) == 3):  # if its 3 digits
        aux = list(pos)
        X = aux[0] + aux[1]  # X = first 2 digits
        Y = aux[2]  # Y = last digit

    else:
        X, Y = list(pos)

    X = 10 - int(X)  # turns X and Y coordinates for the matrix
    Y = string.ascii_lowercase.index(Y)
    return X, Y


def transform_pos(X, Y):
    return str(10 - X) + string.ascii_letters[Y]

def victory(tabuleiro):
    p = 0
    b = 0
    for line in tabuleiro:
        p += line.count('p') + line.count('P')
        b += line.count('b') + line.count('B')

    if p>0 and b == 0:
        return True
    return False


def Can_Capture(tabuleiro):
    for i in range(10):
        for j in range(10):
            if tabuleiro[i][j] == 'p':  # if its a 'p' piece
                if j + 2 < 10:  # if the prediction doesnt goes beyond the size of the board
                    if i - 2 > -1:
                        if tabuleiro[i - 1][j + 1] in ['b', 'B'] and tabuleiro[i - 2][j + 2] == ' ':  # if its diagonal up-right is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                    if i + 2 < 10:
                        if tabuleiro[i + 1][j + 1] in ['b', 'B'] and tabuleiro[i + 2][j + 2] == ' ':  # if its diagonal down-right is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                if j - 2 > -1:  # if the prediction doesnt goes beyond the size of the board
                    if i - 2 > -1:
                        if tabuleiro[i - 1][j - 1] in ['b', 'B'] and tabuleiro[i - 2][j - 2] == ' ':  # if its diagonal up-left is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                    if i + 2 < 10:
                        if tabuleiro[i + 1][j - 1] in ['b', 'B'] and tabuleiro[i + 2][j - 2] == ' ':  # if its diagonal down-left is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            return True

            if tabuleiro[i][j] == 'P':
                for k in range(10):
                    for l in range(10):

                        if Is_Open_Diagonal_Capture(i, j, k, l, tabuleiro)[
                            0]:  # CONFERIR ESPACO VAZIO DEPOIS DA PECA A SER COMIDA
                            return True

    return False


def Possible_Captures(tabuleiro):
    possible_captures = []

    for i in range(10):
        for j in range(10):
            if tabuleiro[i][j] == 'p':  # if its a 'p' piece
                if j + 2 < 10:  # if the prediction doesnt goes beyond the size of the board
                    if i - 2 > -1:
                        if tabuleiro[i - 1][j + 1] in ['b', 'B'] and tabuleiro[i - 2][j + 2] == ' ':  # if its diagonal up-right is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i, j), (i - 2, j + 2)))
                    if i + 2 < 10:
                        if tabuleiro[i + 1][j + 1] in ['b', 'B'] and tabuleiro[i + 2][j + 2] == ' ':  # if its diagonal down-right is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i, j), (i + 2, j + 2)))
                if j - 2 > -1:  # if the prediction doesnt goes beyond the size of the board
                    if i - 2 > -1:
                        if tabuleiro[i - 1][j - 1] in ['b', 'B'] and tabuleiro[i - 2][j - 2] == ' ':  # if its diagonal up-left is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i, j), (i - 2, j - 2)))
                    if i + 2 < 10:
                        if tabuleiro[i + 1][j - 1] in ['b', 'B'] and tabuleiro[i + 2][j - 2] == ' ':  # if its diagonal down-left is an enemy and after it its blank
                            # print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i, j), (i + 2, j - 2)))

            if tabuleiro[i][j] == 'P':
                for k in range(10):
                    for l in range(10):
                        result = Is_Open_Diagonal_Capture(i, j, k, l, tabuleiro)
                        if result[0]:
                            possible_captures.append(((i, j), (k, l)))

    return possible_captures


def Possible_Captures_Piece(tabuleiro, piece):
    X = piece[0]
    Y = piece[1]
    possible_captures = []

    if tabuleiro[X][Y] == 'p':  # if its a 'p' piece
        if Y + 2 < 10:  # if the prediction doesnt goes beyond the size of the board
            if X - 2 > -1:
                if tabuleiro[X - 1][Y + 1] in ['b', 'B'] and tabuleiro[X - 2][Y + 2] == ' ':  # if its diagonal up-right is an enemy and after it its blank
                    # print("can move  " ,10-i,string.ascii_letters[j])
                    possible_captures.append(((X, Y), (X - 2, Y + 2)))
            if X + 2 < 10:
                if tabuleiro[X + 1][Y + 1] in ['b', 'B'] and tabuleiro[X + 2][Y + 2] == ' ':  # if its diagonal down-right is an enemy and after it its blank
                    # print("can move  " ,10-i,string.ascii_letters[j])
                    possible_captures.append(((X, Y), (X + 2, Y + 2)))
        if Y - 2 > -1:  # if the prediction doesnt goes beyond the size of the board
            if X - 2 > -1:
                if tabuleiro[X - 1][Y - 1] in ['b', 'B'] and tabuleiro[X - 2][Y - 2] == ' ':  # if its diagonal up-left is an enemy and after it its blank
                    # print("can move  " ,10-i,string.ascii_letters[j])
                    possible_captures.append(((X, Y), (X - 2, Y - 2)))
            if X + 2 < 10:
                if tabuleiro[X + 1][Y - 1] in ['b', 'B'] and tabuleiro[X + 2][Y - 2] == ' ':  # if its diagonal down-left is an enemy and after it its blank
                    # print("can move  " ,10-i,string.ascii_letters[j])
                    possible_captures.append(((X, Y), (X + 2, Y - 2)))

    if tabuleiro[X][Y] == 'P':
        for k in range(10):
            for l in range(10):
                result = Is_Open_Diagonal_Capture(X, Y, k, l, tabuleiro)
                if result[0]:
                    possible_captures.append(((X, Y), (k, l)))

    return possible_captures


def Maior_Captura3(lista, tabuleiro):
    if len(lista) == 0:
        moves = Possible_Captures(tabuleiro)
    else:
        moves = Possible_Captures_Piece(tabuleiro, lista[-1][1])

    if len(moves) == 0:  # se não há capturas possíveis, retorna a sequencia de movimentos que foi feita até aqui
        return [lista]

    sequence_matrixes = []  # receberá matrizes de melhores movimentos

    for move in moves:  # chama recursão de cada movimento de captura possivel
        copia = deepcopy(tabuleiro)
        Move(transform_pos(move[0][0], move[0][1]), transform_pos(move[1][0], move[1][1]), copia, False)  # faz o movimento
        lista2 = deepcopy(lista)
        lista2.append(move)
        sequence_matrixes.append(
            Maior_Captura3(lista2, copia))  # chama a recursão para o novo estado encontrado, e adiciona o resultado
        # de melhores sequencias

    best_size = 0
    best_sequences = []

    for sequence_list in sequence_matrixes:  # acha a sequencia com tamanho maior
        for sequence in sequence_list:
            if len(sequence) > best_size:
                best_size = len(sequence)

    for sequence_list in sequence_matrixes:  # confere se existem outras sequencias com o mesmo tamanho
        for sequence in sequence_list:
            if len(sequence) > 0 and len(sequence) == best_size:
                best_sequences.append(sequence)

    return best_sequences  # retorna as melhores sequencias possíveis


def Only_Enemy_Between(between):
    for i in range(len(between)):  # sets all to lower
        between[i] = between[i].lower()

    if (between.count('b') == 1 and between.count('p') == 0):
        return True
    return False


def Is_Open_Diagonal_Capture(X, Y, toX, toY, tabuleiro):  # returns if its possible to capture and in what direction
    if (tabuleiro[toX][toY] == ' '):
        if (X - toX == Y - toY) or (-1 * (X - toX) == Y - toY):  # if its diagonal
            if X < toX:
                if Y < toY:  # if its down-right
                    AX = toX - 1
                    AY = toY - 1
                    between = []
                    while (AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX -= 1
                        AY -= 1

                    if (Only_Enemy_Between(between)):
                        return (True, -1, -1)

                elif Y > toY:  # if its down-left
                    AX = toX - 1
                    AY = toY + 1
                    between = []
                    while (AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX -= 1
                        AY += 1

                    if (Only_Enemy_Between(between)):
                        return (True, -1, +1)

            elif X > toX:

                if Y < toY:  # if its up-right
                    AX = toX + 1
                    AY = toY - 1
                    between = []
                    while (AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX += 1
                        AY -= 1

                    if (Only_Enemy_Between(between)):
                        return (True, +1, -1)

                elif Y > toY:  # if its up-left
                    AX = toX + 1
                    AY = toY + 1
                    between = []
                    while (AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX += 1
                        AY += 1

                    if (Only_Enemy_Between(between)):
                        return (True, +1, +1)

    return (False, 0, 0)


def Is_Open_Diagonal(X, Y, toX, toY, tabuleiro):
    if (X - toX == Y - toY) or (-1 * (X - toX) == Y - toY):  # if its diagonal
        if X < toX:
            if Y < toY:  # if its down-right
                AX = toX - 1
                AY = toY - 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX -= 1
                    AY -= 1
                return True

            elif Y > toY:  # if its down-left
                AX = toX - 1
                AY = toY + 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX -= 1
                    AY += 1
                return True
        elif X > toX:
            if Y < toY:  # if its up-right
                AX = toX + 1
                AY = toY - 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX += 1
                    AY -= 1
                return True

            elif Y > toY:  # if its up-left
                AX = toX + 1
                AY = toY + 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX += 1
                    AY += 1
                return True
    return False


def Move(piece, position, tabuleiro, print_move):  # Move("4b","5c")
    X, Y = read_pos(piece)
    toX, toY = read_pos(position)

    can_capture = Can_Capture(tabuleiro)
    moved = False

    selected = tabuleiro[X][Y]

    if tabuleiro[toX][toY] == " ":  # if destiny is empty
        if tabuleiro[X][Y] == 'p':  # and the piece we are moving is a 'p'
            if toX == X + 1 and toY - Y in [1,-1] and not can_capture:  # if cant capture, must move forward(toX must be X-1) and must be one to the left or one to the right(toY-Y = -1 or 1)
                tabuleiro[X][Y] = ' '
                if toX == 9:  # if piece reaches bottom, turns into King
                    selected = 'P'
                tabuleiro[toX][toY] = selected
                moved = True

            elif toX - X in [2, -2] and toY - Y in [2, -2]:  # if its trying to capture
                if toX < X and toY > Y and tabuleiro[X - 1][Y + 1] in ['b','B']:  # if the destiny is up-right, and its diagonal up-right is a 'b'
                    tabuleiro[X][Y] = ' '  # cleans the position selected
                    tabuleiro[X - 1][Y + 1] = ' '  # kills the diagonal enemy piece
                    if toX == 9:  # if piece reaches bottom, turns into King
                        selected = 'P'
                    tabuleiro[toX][toY] = selected  # puts the piece on the destiny position
                    moved = True

                elif toX > X and toY > Y and tabuleiro[X + 1][Y + 1] in ['b', 'B']:  # if the destiny is down-right, and its diagonal down-right is a 'b'
                    tabuleiro[X][Y] = ' '  # cleans the position selected
                    tabuleiro[X + 1][Y + 1] = ' '  # kills the diagonal enemy piece
                    if toX == 9:  # if piece reaches bottom, turns into King
                        selected = 'P'
                    tabuleiro[toX][toY] = selected  # puts the piece on the destiny position
                    moved = True

                elif toX < X and toY < Y and tabuleiro[X - 1][Y - 1] in ['b','B']:  # if the destiny is up-left, and its diagonal up-left is a 'b'
                    tabuleiro[X][Y] = ' '  # cleans the position selected
                    tabuleiro[X - 1][Y - 1] = ' '  # kills the diagonal enemy piece
                    if toX == 9:  # if piece reaches bottom, turns into King
                        selected = 'P'
                    tabuleiro[toX][toY] = selected  # puts the piece on the destiny position
                    moved = True
                elif toX > X and toY < Y and tabuleiro[X + 1][Y - 1] in ['b','B']:  # if the destiny is down-left, and its diagonal down-left is a 'b'
                    tabuleiro[X][Y] = ' '  # cleans the position selected
                    tabuleiro[X + 1][Y - 1] = ' '  # kills the diagonal enemy piece
                    if toX == 9:  # if piece reaches bottom, turns into King
                        selected = 'P'
                    tabuleiro[toX][toY] = selected  # puts the piece on the destiny position
                    moved = True

        elif tabuleiro[X][Y] == 'P':
            if Is_Open_Diagonal(X, Y, toX, toY, tabuleiro) and not can_capture:  # if cant capture, must move diagonaly
                tabuleiro[X][Y] = ' '
                tabuleiro[toX][toY] = selected
                moved = True

            else:
                result = Is_Open_Diagonal_Capture(X, Y, toX, toY, tabuleiro)  # what direction it can capture

                if (result[0]):

                    dx = result[1]
                    dy = result[2]

                    aux_X = toX + dx
                    aux_Y = toY + dy

                    between_coord = []  # the position of the p and P between destiny and piece

                    while (aux_X != X and aux_Y != Y):
                        if (tabuleiro[aux_X][aux_Y] in ['b', 'B']):  # if its a p or P, saves its coordinates
                            between_coord.append((aux_X, aux_Y))
                        aux_X += dx
                        aux_Y += dy

                    tabuleiro[X][Y] = ' '
                    tabuleiro[between_coord[0][0]][between_coord[0][1]] = ' '
                    tabuleiro[toX][toY] = selected
                    moved = True

    if (print_move):
        print("==================================================")
        if (can_capture and not moved):
            print("movimento impossível, jogador deve obrigatoriamente eliminar uma peça adversária quando possível")
        elif (not moved):
            print("movimento impossível")
        if (moved):
            print("Computador moveu de ", piece, "para ", position)

    return moved


def Print_Board(tabuleiro):
    print(10, " |", end=" ")
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            print(tabuleiro[i][j], "|", end=" ")
        print()
        if (i != 9):
            print(9 - i, "  |", end=" ")
    print()
    print("      A   B   C   D   E   F   G   H   I   J")


def Print_Moves(resultado):
    counter = 1
    for move in resultado:
        print("sequencia", counter)
        counter += 1
        for step in move:
            if (step == move[0]):
                print(transform_pos(step[0][0], step[0][1]), "->",transform_pos(step[1][0], step[1][1]), end=" ")
            else:
                print("->", transform_pos(step[1][0], step[1][1]), end=" ")
        print("\n")

def Best_Move(tabuleiro):

    B_move = Minimax.minimax_decision(tabuleiro,5)
    return B_move

""""
pega posicao
    ve quais movimentos sao possiveis
    para cada movimento posivel (lista)
        cria tupla de cada movimento do inimigo
            seta heuristic de cada move do inimigo
        define 

    pega o menor heuristic e joga
"""