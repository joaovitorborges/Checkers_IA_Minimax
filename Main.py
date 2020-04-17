import Damas

Estado_inicial = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', 'p', ' ', 'p', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]



print("CHECKERS")
while(True):
    resultado = Damas.Maior_Captura2([],Estado_inicial)
    print("tam resultado:",len(resultado))

    for move in resultado:
        print(Damas.transform_pos(move[0][0],move[0][1]),Damas.transform_pos(move[1][0],move[1][1]))


    Damas.Print_Board(Estado_inicial)
    player_moved = False
    while(not player_moved):
        #movimento[] = mais_comidas()
        player_moved = Damas.Player_Move(input(), input(),Estado_inicial)
    #Computer_Move()