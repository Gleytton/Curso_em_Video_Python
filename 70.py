soma = 0

contp = 0


min = 9999

while True:

    nome = str(input('Nome do produto: '))

    preco = float(input('Preço: '))

    soma += preco

    if preco >= 1000:

        contp += 1

    if preco < min:

        min = preco

        aux = nome


    opcao = str(input('Deseja inserir mais produtos (Sim - S / Não - N): '))

    if opcao in 'Nn':

        print('Total da compra: {}'.format(soma))

        print('Produtos com preço maior que R$ 1.000,00: {}'.format(contp))

        print('Produto mais barato: {}'.format(aux))

        break



