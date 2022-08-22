from random import randrange


def sortear(lista):

    for i in range(0, 5):

        lista.append(randrange(0, 51))

    print(lista)

def somaPar(lista):

    soma = 0
    for i in range (0, 5):

        if lista[i] % 2 == 0:

            soma += lista[i]

    print("A soma dos pares será: {}".format(soma))

numero = list()

sortear(numero)

somaPar(numero)