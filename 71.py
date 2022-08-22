import random


while True:

    valor = int(input('Digite o valor desejado ( NOTAS: 2, 5, 10, 20, 50): '))

    soma = 0

    moeda = ['2', '5','10','20','50']

    while soma < valor:

        aux = int(random.choice(moeda))

        soma += aux

        print(aux)

