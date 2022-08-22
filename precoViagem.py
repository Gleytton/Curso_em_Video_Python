distancia = float(input('Distância do destino (em Km): '))

if(distancia <= 200):

    preco = distancia * 0.50
    print('Total da viagem: R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Total da viagem: R${:.2f}'.format(preco))