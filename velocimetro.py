velocidade = int(input('Entre com a velocidade do veículo: '))

if(velocidade >= 80):
    print('Você foi multado!!')
    multa = (velocidade - 80)*7
    print('Valor a pagar: R${:.2f}'.format(multa))
else:
    print('Boa viagem!')