numero = int(input('Digite um número: '))

print('Digite: 1 - Binário   2 - Octal   3 - Hexadecimal'  )

opcao = int(input('Escolha uma opcao: '))

if( opcao == 1):
    print('O numero {} em binário é: {%}'.format(numero, bin(numero))

if( opcao == 2):
    print('O numero {} em octal é: {%o}'.format(numero, oct(numero))

if(opcao == 3):
    print('O numero {} em hexadecimal é: {:%x}'.format(numero, hex(numero))

