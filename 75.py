numero = ['','','','','']

for i in range (0,5):

   print(i)

   numero[i] = input('Digite um determinado valor:')

for i in range (0,5):

    aux = str(numero[i])

    cont = aux.count('9')

    print('O número {} tem {} números 9'.format(numero[i], cont))

for i in range (0,5):

    aux = str(numero[i])

    if aux.count('3') != 0:

        pos = aux.index('3')

        print('O número {} tem o numero 3 na posicao {}'.format(numero[i], pos))
    else:

        print('O número {} não possui o algarismo 3')


for i in range (0,5):

    numero[i] = int(numero[i])

    if numero[i] % 2 == 0:

        print('Numeros pares:{}'.format(numero[i]))
    else:

        print('Não existem números pares')