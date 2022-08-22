import random

lista = [0,0,0,0,0]

for i in range (0,5):

    num = random.randint(0,100)

    lista[i] = num

print (lista)

lista = tuple(lista)

print (lista)

maior = -9999

menor = 9999

for i in range (0,5):

    if lista [i] > maior:

        maior = lista [i]

    if lista [i] < menor:

        menor  = lista [i]

print ('Maior: {}'.format(maior))

print ('Menor: {}'.format(menor))