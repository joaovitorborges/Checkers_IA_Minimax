import string

tabuleiro = [[' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
             ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
             [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
             ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['p', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
             ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
             [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
             ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ']]


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

def Player_Move(piece, position):

        X,Y = read_pos(piece)
        toX,toY = read_pos(position)

        moved = False

        print("movement: piece from ",X,Y,"  to ",toX,toY)

        if tabuleiro[toX][toY] ==" ":               # if destiny is empty
            if tabuleiro[X][Y] == 'b':              # and the piece we are moving is a 'b'
                if toX==X-1 and toY-Y in [1,-1]:    # must move forward(toX must be X-1) and must be one to the left or one to the right(toY-Y = -1 or 1)
                    tabuleiro[X][Y] = ' '
                    tabuleiro[toX][toY] = 'b'
                    moved = True

                elif toX == X-2 and toY-Y in[2,-2]:
                    if toY > Y and tabuleiro[X-1][Y+1] == 'p':     # if the destiny is to the right, and its diagonal right is a 'p'
                        tabuleiro[X][Y] = ' '                      # cleans the position selected
                        tabuleiro[X-1][Y+1] = ' '                  # kills the diagonal enemy piece
                        tabuleiro[toX][toY] = 'b'                  # puts the piece on the destiny position
                        moved = True

                    elif toY < Y and tabuleiro[X-1][Y-1] == 'p':   # if the destiny is to the left, and its diagonal left is a 'p'
                        print(tabuleiro[X-1][Y-1])
                        tabuleiro[X][Y] = ' '                      # cleans the position selected
                        tabuleiro[X-1][Y-1] = ' '                  # kills the diagonal enemy piece
                        tabuleiro[toX][toY] = 'b'                  # puts the piece on the destiny position
                        moved = True


            elif tabuleiro[X][Y] == 'B':
                print("tem q fazer kk")
                 #to do

        if(not moved):
            print("movimento impossível")


#Move("4b","5c")
#6d
#4d 6b

def Print_Board():
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            print(tabuleiro[i][j],"|",end = " ")
        print()

""""
pega posicao
    ve quais movimentos sao possiveis
    para cada movimento posivel (lista)
        cria tupla de cada movimento do inimigo
            seta heuristic de cada move do inimigo
        define 
    
    pega o menor heuristic e joga
"""

while(True):
    print("CHECKERS")
    Print_Board()
    Player_Move(input(), input())