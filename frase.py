frase = str(input('Digite uma frase: '))

print('A frase tem {}'.format(frase.upper().count('A')))
print('A primeira letra "A" aparece na posicao {}'.format(frase.upper().find('A')))
print('A ultima letra "A" aparece na posicao {}'.format(frase.upper().rfind('A')))