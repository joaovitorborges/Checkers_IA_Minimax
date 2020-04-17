import string
from copy import deepcopy
#from anytree import Node, RenderTree

def read_pos(pos):          # read inputs such as "9c" or "10d" and return them as coordinates

    if (len(pos) == 3):                    # if its 3 digits
        aux = list(pos)
        X = aux[0] + aux[1]                # X = first 2 digits
        Y = aux[2]                         # Y = last digit

    else:
        X, Y = list(pos)

    X = 10 - int(X)                       # turns X and Y coordinates for the matrix
    Y = string.ascii_lowercase.index(Y)
    return X,Y

def transform_pos(X,Y):
    return str(10-X) + string.ascii_letters[Y]

def Player_Can_Capture(tabuleiro):
    for i in range(10):
        for j in range(10):
            if tabuleiro[i][j] == 'b':                                                 # if its a 'b' piece
                if j+2 < 10 :                                                          # if the prediction doesnt goes beyond the size of the board
                    if i-2 >-1:
                        if tabuleiro[i-1][j+1] in ['p','P'] and tabuleiro[i-2][j+2] == ' ':  # if its diagonal up-right is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                    if i + 2 < 10:
                        if tabuleiro[i+1][j+1] in ['p','P'] and tabuleiro[i+2][j+2] == ' ':  # if its diagonal down-right is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                if j-2 > -1:                                                           # if the prediction doesnt goes beyond the size of the board
                    if i-2 >-1:
                        if tabuleiro[i-1][j-1] in ['p','P'] and tabuleiro[i-2][j-2] == ' ':  # if its diagonal up-left is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                    if i + 2 < 10:
                        if tabuleiro[i+1][j-1] in ['p','P'] and tabuleiro[i+2][j-2] == ' ':  # if its diagonal down-left is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True


            if tabuleiro[i][j] == 'B':
                for k in range(10):
                    for l in range(10):

                        if Is_Open_Diagonal_Capture(i,j,k,l,tabuleiro)[0]:  #CONFERIR ESPACO VAZIO DEPOIS DA PECA A SER COMIDA
                            return True

    return False

def Possible_Captures(tabuleiro):
    possible_captures = []

    for i in range(10):
        for j in range(10):
            if tabuleiro[i][j] == 'b':                                                 # if its a 'b' piece
                if j+2 < 10 :                                                          # if the prediction doesnt goes beyond the size of the board
                    if i-2 >-1:
                        if tabuleiro[i-1][j+1] in ['p','P'] and tabuleiro[i-2][j+2] == ' ':  # if its diagonal up-right is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i,j),(i-2,j+2)))
                    if i + 2 < 10:
                        if tabuleiro[i+1][j+1] in ['p','P'] and tabuleiro[i+2][j+2] == ' ':  # if its diagonal down-right is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i,j),(i+2,j+2)))
                if j-2 > -1:                                                           # if the prediction doesnt goes beyond the size of the board
                    if i-2 >-1:
                        if tabuleiro[i-1][j-1] in ['p','P'] and tabuleiro[i-2][j-2] == ' ':  # if its diagonal up-left is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i,j),(i-2,j-2)))
                    if i + 2 < 10:
                        if tabuleiro[i+1][j-1] in ['p','P'] and tabuleiro[i+2][j-2] == ' ':  # if its diagonal down-left is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            possible_captures.append(((i,j),(i+2,j-2)))


            if tabuleiro[i][j] == 'B':
                for k in range(10):
                    for l in range(10):
                        result = Is_Open_Diagonal_Capture(i,j,k,l,tabuleiro)
                        if result[0]:
                            possible_captures.append(((i,j),(k,l)))

    return possible_captures

def Maior_Captura(lista,c,tabuleiro):

    moves = Possible_Captures(tabuleiro)

    M = c
    Bmove = ()

    for move in moves:
        copia = deepcopy(tabuleiro)
        Player_Move(transform_pos(move[0][0],move[0][1]),transform_pos(move[1][0],move[1][1]),copia)
        R = Maior_Captura(lista,c+1,copia)
        if R > M:
            M = R
            Bmove = move

    if Bmove != ():
        lista.append(Bmove)
    return M

def Maior_Captura2(lista,tabuleiro):

    moves = Possible_Captures(tabuleiro)

    if len(moves) == 0:
        return lista

    sequence_list = []

    for move in moves:
        copia = deepcopy(tabuleiro)
        Player_Move(transform_pos(move[0][0],move[0][1]),transform_pos(move[1][0],move[1][1]),copia)
        lista2 = deepcopy(lista)
        lista2.append(move)
        sequence_list.append(Maior_Captura2(lista2,copia))

    B = 0
    B_sequence = []

    for sequence in sequence_list:
        if len(sequence) > B:
            B = len(sequence)
            B_sequence = sequence

    return B_sequence



def Only_Enemy_Between(between):
    for i in range(len(between)):  # sets all to lower
        between[i] = between[i].lower()

    if (between.count('p') == 1 and between.count('b') == 0):
        return True
    return False

def Is_Open_Diagonal_Capture(X,Y,toX,toY,tabuleiro):   # returns if its possible to capture and in what direction
    if (tabuleiro[toX][toY] == ' '):
        if (X-toX == Y - toY) or (-1*(X-toX) == Y - toY):      # if its diagonal
            if X < toX:
                if Y < toY:       # if its down-right
                    AX = toX-1
                    AY = toY-1
                    between = []
                    while(AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX -= 1
                        AY -= 1

                    if(Only_Enemy_Between(between)):
                        return (True, -1, -1)

                elif Y > toY:     # if its down-left
                    AX = toX - 1
                    AY = toY + 1
                    between = []
                    while (AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX -= 1
                        AY += 1

                    if(Only_Enemy_Between(between)):
                        return (True, -1, +1)

            elif X > toX:

                if Y < toY:       # if its up-right
                    AX = toX + 1
                    AY = toY - 1
                    between = []
                    while (AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX += 1
                        AY -= 1

                    if(Only_Enemy_Between(between)):
                        return (True,+1,-1)

                elif Y > toY:     # if its up-left
                    AX = toX + 1
                    AY = toY + 1
                    between = []
                    while (AX != X and AY != Y):
                        between.append(tabuleiro[AX][AY])
                        AX += 1
                        AY += 1

                    if (Only_Enemy_Between(between)):
                        return (True,+1,+1)

    return (False,0,0)

def Is_Open_Diagonal(X,Y,toX,toY,tabuleiro):
    if (X-toX == Y - toY) or (-1*(X-toX) == Y - toY) :      # if its diagonal
        if X < toX:
            if Y < toY:       # if its down-right
                AX = toX-1
                AY = toY-1
                while(AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX -= 1
                    AY -= 1
                return True

            elif Y > toY:     # if its down-left
                AX = toX - 1
                AY = toY + 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX -= 1
                    AY += 1
                return True
        elif X > toX:
            if Y < toY:       # if its up-right
                AX = toX + 1
                AY = toY - 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX += 1
                    AY -= 1
                return True

            elif Y > toY:     # if its up-left
                AX = toX + 1
                AY = toY + 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return False
                    AX += 1
                    AY += 1
                return True
    return False



def Player_Move(piece, position, tabuleiro):  #Move("4b","5c")
        X,Y = read_pos(piece)
        toX,toY = read_pos(position)

        can_capture = Player_Can_Capture(tabuleiro)
        moved = False

        selected = tabuleiro[X][Y]

        if tabuleiro[toX][toY] ==" ":                                  # if destiny is empty
            if tabuleiro[X][Y] == 'b':                                 # and the piece we are moving is a 'b'
                if toX==X-1 and toY-Y in [1,-1] and not can_capture:   #  if cant capture, must move forward(toX must be X-1) and must be one to the left or one to the right(toY-Y = -1 or 1)
                    tabuleiro[X][Y] = ' '
                    if toX == 0:                                    # if piece reaches top, turns into King
                        selected = 'B'
                    tabuleiro[toX][toY] = selected
                    moved = True

                elif toX == X-2 and toY-Y in[2,-2]:
                    if toY > Y and tabuleiro[X-1][Y+1] in ['p','P']:     # if the destiny is to the right, and its diagonal right is a 'p'
                        tabuleiro[X][Y] = ' '                      # cleans the position selected
                        tabuleiro[X-1][Y+1] = ' '                  # kills the diagonal enemy piece
                        if toX == 0:  # if piece reaches top, turns into King
                            selected = 'B'
                        tabuleiro[toX][toY] = selected             # puts the piece on the destiny position
                        moved = True


                    elif toY < Y and tabuleiro[X-1][Y-1] in ['p','P']:   # if the destiny is to the left, and its diagonal left is a 'p'
                        print(tabuleiro[X-1][Y-1])
                        tabuleiro[X][Y] = ' '                      # cleans the position selected
                        tabuleiro[X-1][Y-1] = ' '                  # kills the diagonal enemy piece
                        if toX == 0:  # if piece reaches top, turns into King
                            selected = 'B'
                        tabuleiro[toX][toY] = selected             # puts the piece on the destiny position
                        moved = True


            elif tabuleiro[X][Y] == 'B':
                if Is_Open_Diagonal(X,Y,toX,toY,tabuleiro) and not can_capture:  # if cant capture, must move diagonaly
                    tabuleiro[X][Y] = ' '
                    tabuleiro[toX][toY] = selected
                    moved = True

                else:
                    result = Is_Open_Diagonal_Capture(X, Y, toX, toY,tabuleiro)  # what direction it can capture

                    if(result[0]):

                        dx = result[1]
                        dy = result[2]

                        aux_X = toX+dx
                        aux_Y = toY+dy


                        between_coord = []  #  the position of the p and P between destiny and piece

                        while(aux_X!=X and aux_Y!=Y):
                            if(tabuleiro[aux_X][aux_Y] in ['p','P']):   # if its a p or P, saves its coordinates
                                between_coord.append((aux_X,aux_Y))
                            aux_X += dx
                            aux_Y += dy


                        tabuleiro[X][Y] = ' '
                        tabuleiro[between_coord[0][0]][between_coord[0][1]] = ' '
                        tabuleiro[toX][toY] = selected
                        moved = True




        print("==================================================")
        if(can_capture and not moved):
            print("movimento impossível, jogador deve obrigatoriamente eliminar uma peça adversária quando possível")
        elif(not moved):
            print("movimento impossível")
        if(moved):
            print("Jogador moveu de ",piece, "para ",position )
        return moved

def Print_Board(tabuleiro):
    print(10, " |", end=" ")
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            print(tabuleiro[i][j],"|",end = " ")
        print()
        if(i != 9):
            print(9 - i, "  |", end=" ")
    print()
    print("      A   B   C   D   E   F   G   H   I   J")

""""
pega posicao
    ve quais movimentos sao possiveis
    para cada movimento posivel (lista)
        cria tupla de cada movimento do inimigo
            seta heuristic de cada move do inimigo
        define 
    
    pega o menor heuristic e joga
"""