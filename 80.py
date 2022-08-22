vet =  list(range(0,5))

menor = 9999

maior = -9999

    for cont in range (0,5):

        num =  int(input('Digite um inteiro: '))

        if num >= maior:

            vet.insert(4,num)

        if num < menor:

            vet.insert(0, num)


print(vet)
