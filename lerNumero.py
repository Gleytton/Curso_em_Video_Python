num = int(input('Digite um numero inteiro: '))

cont = 1

soma = num

while num < 999:

    num = int(input('Digite um numero inteiro: '))

    if num < 999:

        cont += 1

    if num < 999:

        soma += num


print('Números digitados: {}'.format(cont))
print('Soma {}'.format(soma))


