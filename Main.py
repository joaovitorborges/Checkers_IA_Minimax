import Player, Computer
import time

Estado_inicial =  [[' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
                   ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
                   [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
                   ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
                   ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
                   [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
                   ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ']]




print("CHECKERS")
print("TURNO DO JOGADOR")
Player.Print_Board(Estado_inicial)
print()
while(True):

    player_moved = False
    while(not player_moved):
        if Player.Can_Capture(Estado_inicial):
            print("O jogador precisa capturar uma ou mais peças adversárias, escolha uma sequência:")

            resultado = Player.Maior_Captura3([], Estado_inicial)

            counter = 1
            for move in resultado:
                print("sequencia", counter)
                counter += 1
                for step in move:
                    if (step == move[0]):
                        print(Player.transform_pos(step[0][0], step[0][1]), "->", Player.transform_pos(step[1][0], step[1][1]), end=" ")
                    else:
                        print("->", Player.transform_pos(step[1][0], step[1][1]), end=" ")
                print("\n")


            escolha = input()

            while not str.isdigit(escolha) or not 0<int(escolha)<counter:
                print("escolha uma sequência válida")
                escolha = input()

            escolha = int(escolha)



            move_choice = resultado[escolha-1]

            for step in move_choice:
                player_moved = Player.Move(Player.transform_pos(step[0][0], step[0][1]), Player.transform_pos(step[1][0], step[1][1]), Estado_inicial, False)
            #player_moved = Damas.Player_Move(input("Mover peça:"), input("para:"), Estado_inicial,True)
        else:
            peça = input("Mover peça:")
            para = input("para:")
            #WHILE VERIFICAR
            player_moved = Player.Move(peça, para, Estado_inicial, True)

    Player.Print_Board(Estado_inicial)
    if Player.victory(Estado_inicial):
        print("VITÓRIA DO JOGADOR!")
        break
    input("pressione enter para passar para o turno do computador")
    print("Pensando...")

    start = time.time()
    Move = Computer.Best_Move(Estado_inicial)
    end = time.time()
    print("tempo decorrido:",end-start)
    print()
    print(Move)
    if isinstance(Move,list):
        for step in Move:
            Computer.Move(Computer.transform_pos(step[0][0], step[0][1]),Computer.transform_pos(step[1][0], step[1][1]), Estado_inicial, True)
    else:
        Computer.Move(Computer.transform_pos(Move[0][0], Move[0][1]),Computer.transform_pos(Move[1][0], Move[1][1]),Estado_inicial,True)
    Computer.Print_Board(Estado_inicial)
    if Computer.victory(Estado_inicial):
        print("VITÓRIA DO JOGADOR!")
        break