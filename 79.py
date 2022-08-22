num = list()

cont = 0

new_num = (input('Digite um inteiro: '))
print('Numero adicionado com sucesso!!!')
num.append(new_num)
cont += 1
opcao = input(str('Deseja inserir um numero (S/N): '))

while(opcao == 'S'):

    new_num = (input('Digite um inteiro: '))


    if (new_num in num):
        print("Esse número já foi adicionado a lista!!!")
        opcao = input(str('Deseja inserir um numero (S/N): '))

    else:
        print('Numero adicionado com sucesso!!!')
        cont += 1
        opcao = input(str('Deseja inserir um numero (S/N): '))


print(num.sort())