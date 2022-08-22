a1 = int(input('Digite o primeiro termo da PA: '))

razao = int(input('Digite a razao da PA: '))

n = 1

limite = 11

while n != limite:

    if n != limite:

        termo = a1 + (n - 1)*razao

        print(termo)

        n += 1

    if n == limite:

        aux = int(input('Deseja exibir mais quantos termos: '))

        n = 1

        if aux != 0:

            limite += aux

        if aux == 0:

            exit()









