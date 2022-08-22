num = int(input('Digite um número inteiro: '))

aux = 1

fat = 1

while aux != (num + 1):

    fat *= aux
    aux += 1

print('Fatorial de {} = {}'.format(num,fat))
