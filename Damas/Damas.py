import string


tabuleiro = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


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

def Player_Can_Capture(tabuleiro):
    for i in range(10):
        for j in range(10):
            if tabuleiro[i][j] == 'b':                                                 # if its a 'b' piece
                if j+2 < 10 :                                                          # if the prediction doesnt goes beyond the size of the board
                    if i-2 >-1:
                        if tabuleiro[i-1][j+1] == 'p' and tabuleiro[i-2][j+2] == ' ':  # if its diagonal up-right is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                    if i + 2 < 10:
                        if tabuleiro[i+1][j+1] == 'p' and tabuleiro[i+2][j+2] == ' ':  # if its diagonal down-right is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                if j-2 > -1:                                                           # if the prediction doesnt goes beyond the size of the board
                    if i-2 >-1:
                        if tabuleiro[i-1][j-1] == 'p' and tabuleiro[i-2][j-2] == ' ':  # if its diagonal up-left is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True
                    if i + 2 < 10:
                        if tabuleiro[i+1][j-1] == 'p' and tabuleiro[i+2][j-2] == ' ':  # if its diagonal down-left is an enemy and after it its blank
                            #print("can move  " ,10-i,string.ascii_letters[j])
                            return True


            if tabuleiro[i][j] == 'B':
                for k in range(10):
                    for l in range(10):

                        if tabuleiro[k][l] == 'p' and Is_Open_Diagonal_Capture(i,j,k,l)[0]:  #CONFERIR ESPACO VAZIO DEPOIS DA PECA A SER COMIDA
                            return True

    return False

def Is_Open_Diagonal_Capture(X,Y,toX,toY):   # returns if its possible to capture and what direction it can

    if (X-toX == Y - toY) or (-1*(X-toX) == Y - toY) :      # if its diagonal
        if X < toX:
            if Y < toY:       # if its down-right
                AX = toX-1
                AY = toY-1
                while(AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return (False,-1,-1)
                    AX -= 1
                    AY -= 1
                if toX+1 < 10 and toY+1 < 10:
                    if(tabuleiro[toX+1][toY+1] == ' '):  # and can move after the enemy piece
                        return (True,-1,-1)

            elif Y > toY:     # if its down-left
                AX = toX - 1
                AY = toY + 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return (False,-1,+1)
                    AX -= 1
                    AY += 1
                if toX + 1 < 10 and toY - 1 > -1:
                    if (tabuleiro[toX + 1][toY - 1] == ' '):  # and can move after the enemy piece
                        return (True,-1,+1)
        elif X > toX:

            if Y < toY:       # if its up-right
                AX = toX + 1
                AY = toY - 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return (False,+1,-1)
                    AX += 1
                    AY -= 1
                if toX - 1 > -1 and toY + 1 < 10:
                    if (tabuleiro[toX - 1][toY + 1] == ' '): # and can move after the enemy piece
                        return (True,+1,-1)

            elif Y > toY:     # if its up-left
                AX = toX + 1
                AY = toY + 1
                while (AX != X and AY != Y):
                    if tabuleiro[AX][AY] != ' ':
                        return (False,+1,+1)
                    AX += 1
                    AY += 1
                if toX - 1 > -1 and toY - 1 > -1:
                    if (tabuleiro[toX - 1][toY - 1] == ' '): # and can move after the enemy piece
                        return (True,+1,+1)

    return (False,0,0)

def Is_Open_Diagonal(X,Y,toX,toY):
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


def Player_Move(piece, position):  #Move("4b","5c")
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
                    if toY > Y and tabuleiro[X-1][Y+1] == 'p':     # if the destiny is to the right, and its diagonal right is a 'p'
                        tabuleiro[X][Y] = ' '                      # cleans the position selected
                        tabuleiro[X-1][Y+1] = ' '                  # kills the diagonal enemy piece
                        if toX == 0:  # if piece reaches top, turns into King
                            selected = 'B'
                        tabuleiro[toX][toY] = selected             # puts the piece on the destiny position
                        moved = True


                    elif toY < Y and tabuleiro[X-1][Y-1] == 'p':   # if the destiny is to the left, and its diagonal left is a 'p'
                        print(tabuleiro[X-1][Y-1])
                        tabuleiro[X][Y] = ' '                      # cleans the position selected
                        tabuleiro[X-1][Y-1] = ' '                  # kills the diagonal enemy piece
                        if toX == 0:  # if piece reaches top, turns into King
                            selected = 'B'
                        tabuleiro[toX][toY] = selected             # puts the piece on the destiny position
                        moved = True


            elif tabuleiro[X][Y] == 'B':
                if Is_Open_Diagonal(X,Y,toX,toY) and not can_capture:  # if cant capture, must move diagonaly
                    tabuleiro[X][Y] = ' '
                    tabuleiro[toX][toY] = selected
                    moved = True

                else:
                    result = Is_Open_Diagonal_Capture(X, Y, toX, toY)  # what direction it can capture
                    dx = result[1]
                    dy = result[2]

                    aux_X = toX+dx
                    aux_Y = toY+dy

                    between = []        #  whats between the destiny and the piece
                    between_coord = []  #  the position of the p and P between destiny and piece

                    while(aux_X!=X and aux_Y!=Y):
                        between.append(tabuleiro[aux_X][aux_Y])      # adds all that is between destiny and piece
                        if(tabuleiro[aux_X][aux_Y] == 'p' or 'P'):   # if its a p or P, saves its coordinates
                            between_coord.append((aux_X,aux_Y))
                        aux_X += dx
                        aux_Y += dy


                    for i in range(len(between)):       # sets all to lower
                        between[i] = between[i].lower()

                    #print(between)
                    if(between.count('p')==1 and between.count('b') == 0): # only moves and captures if theres only one enemy piece between piece and destiny
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


def Print_Board():
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



print("CHECKERS")
while(True):
    Print_Board()

    player_moved = False
    while(not player_moved):
        player_moved = Player_Move(input(), input())
    #Computer_Move()