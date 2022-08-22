nome = str(input('Digite o nome completo:'))

print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))

nome1 = nome.split()

quantidade = len(nome1)

i = 0
somai = 0
while (i != quantidade):
    somai = somai + len(nome1[i])
    i = i+1
print('O nome {} possui {} letras'.format(nome,somai))

j = 0
somaj = 0
while (j < 1):
    somaj = somaj + len(nome1[0])
    j = j +1
print('O nome {} tem {} letras'.format(nome1[0],somaj))



