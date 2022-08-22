completo = str(input('Digite o nome completo: '))

completo = completo.split()

print('O nome é: {}'.format(completo[0]))
print('O ultimo nome é: {}'.format(completo[len(completo) - 1]))