import random

num = 1
cont = 0
while num != 0:
    pc = random.randrange(0,10)

    player = int(input('Digite o número que o computador escolheu (0,10):'))

    if pc == player:
        cont+=1
        num -=1

    else:
        cont+=1
        print('Tente novamente!')
        print('Numero sorteado: {}'.format(pc))

print('O jogador fez {} tentativas'.format(cont))