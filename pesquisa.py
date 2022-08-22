soma = 0

for i in range(1,5,1):

    nome = str(input('Digite o nome da {}° pessoa: '.format(i)))
    sexo = str(input('Sexo da {}° pessoa (M ou F): '.format(i)))
    idade = int(input('Digite a idade da {}° pessoa: '.format(i)))

    soma += idade

    if