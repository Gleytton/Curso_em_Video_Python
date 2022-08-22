num1 = int(input('Digite o primeiro número: '))

num2 = int(input('Digite o segundo número: '))

print('''Escolha uma operacao:

[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')

oper = int(input('Escolha uma operaçao: '))

soma = 0
mult = 1
maior = 0

while oper != 5:

    if oper == 1:

        soma = num1 + num2

        print(soma)

        oper = 0

    if oper == 2:

        mult = num1 * num2

        print(mult)

        oper = 0

    if oper == 3:

        if num1 >= num2:

            maior = num1

            oper = 0

            print('Maior: {}'.format(maior))

        else:

            maior = num2

            oper = 0

            print('Maior: {}'.format(maior))

    if oper == 4:

        new_num = input('Digite um novo número: ')

        oper = 0

    if oper < 0 or oper > 5:

        print('Entrada Inválida!')
        oper = int(input('Escolha uma operaçao: '))

        oper = 0






