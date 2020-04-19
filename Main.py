import Damas

Estado_inicial = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', 'B', ' ', 'b', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', 'p', ' ', 'p', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]



print("CHECKERS")
while(True):
    #print(Damas.Possible_Captures(Estado_inicial))
    print("TURNO DO JOGADOR")
    Damas.Print_Board(Estado_inicial)
    print()
    player_moved = False
    while(not player_moved):
        if Damas.Player_Can_Capture(Estado_inicial):
            print("O jogador precisa capturar uma ou mais peças adversárias, escolha uma sequência:")

            resultado = Damas.Maior_Captura3([], Estado_inicial)

            counter = 1
            for move in resultado:
                print("sequencia", counter)
                counter += 1
                for step in move:
                    if (step == move[0]):
                        print(Damas.transform_pos(step[0][0], step[0][1]), "->",
                              Damas.transform_pos(step[1][0], step[1][1]), end=" ")
                    else:
                        print("->", Damas.transform_pos(step[1][0], step[1][1]), end=" ")
                print("\n")


            escolha = int(input()) # COLOCAR EM UM TRY - CATCH

            while not 0<escolha<counter :
                print("Escolha uma sequencia válida")
                escolha = int(input())

            move_choice = resultado[escolha-1]

            for step in move_choice:
                player_moved = Damas.Player_Move(Damas.transform_pos(step[0][0], step[0][1]), Damas.transform_pos(step[1][0], step[1][1]), Estado_inicial, False)

            #player_moved = Damas.Player_Move(input("Mover peça:"), input("para:"), Estado_inicial,True)
        else:
            player_moved = Damas.Player_Move(input("Mover peça:"), input("para:"),Estado_inicial,True)

    #Computer_Move()