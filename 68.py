import random

cont = 0

while True:



    esc = str(input('Escolha par ou impar (P/I): '))

    esc = esc.upper()

    num = int(input('Digite um numro: '))

    comp = random.randrange(0,11)

    print('O computador escolheu: {}'.format(comp))

    soma = num + comp

    if esc == 'P':

        if soma % 2 == 0:

            cont += 1

            print('Você venceu!!!')

            print('Número de vitórias: {}'.format(cont))
        else:

            print('Número de vitórias consecutivas: {}'.format(cont))

            break

    if esc == 'I':

        if soma % 2 != 0:

            cont += 1

            print('Você venceu!!!!')

            print('Número de vitórias: {}'.format(cont))

        else:

            print('Numero de vitórias consecutivas: {}'.format(cont))

            break