import random

print('Digite [1] - Pedra [2] - Papel  [3] - Tesoura  ')

player = int(input('Sua jogada: '))

pc = random.randrange(1,4,1)

if( player == 1 and pc == 2):

    print('''player = Pedra
    
            pc = Papel
            
            Pc venceu!!!''')

elif( player == 1 and pc == 3):

    print('''player = Pedra

            pc = Tesoura

            Player venceu!!!''')

elif(player == 1  and pc == 1):

    print('''player = Pedra

                pc = Pedra

                EMPATE!!!''')

if(player == 2 and pc == 1):

    print('''player = Papel

                pc = Pedra

                Player venceu!!!''')

elif(player == 2 and pc == 3):

    print('''player = Papel

                pc = Tesoura

                Pc venceu!!!''')

elif( player == pc):

    print('''player = Papel

                pc = Papel

               EMPATE !!!''')

if( player == 3  and pc == 1):

    print('''player = Tesoura

                    pc = Pedra
                    
                   Pc venceu !!!''')

elif( player == 3 and pc == 2):

    print('''player = Tesoura

                    pc = Papel

                   Player venceu !!!''')

elif (player == pc):

    print('''player = Tesoura

                    pc = Tesoura

                   EMPATE !!!''')