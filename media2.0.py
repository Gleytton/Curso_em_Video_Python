cond = 0

soma = 0

cont = 0

max = -9999

min = 9999

while cond == 0:

    num = int(input('Digite um numero: '))

    cont += 1

    soma += num

    if num > max:

        max = num

    if num < min:

        min = num

    media = soma/ num

    verif = str(input('Deseja digitar outro numero (S - sim / N - Não): '))

    verif = verif.upper()

    if verif == 'N':

        cond = 1

print('A média dos numeros digitados foi: {}'.format(media))

print('Valor máximo: {}'.format(max))

print('Valor mínimo: {}'.format(min))