num = list()

maior = -9999

pos_maior = 0

menor = 9999

pos_menor = 0

for cont in range (0,5):

    num.append(int(input('Digite um numero inteiro:')))


for i in range (0,5):

    if num[i] > maior:

        maior = num[i]

        pos_maior = i

    if num [i] < menor:

        menor = num[i]

        pos_menor = i

print('O maior número é {} na posicao {}'.format(maior, pos_maior))

print('O menor número é {} na posicao {}'.format(menor, pos_menor))