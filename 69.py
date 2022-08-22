cont_idade = 0

cont_M = 0

cont_IF = 0

while True:

    idade = int(input('Digite a idade: '))

    sexo = str(input('Digite o sexo (M/F): '))

    if idade >= 18:

        cont_idade += 1



    if sexo == 'M':

        cont_M += 1



    if sexo == 'F':

        if idade < 20:

            cont_IF += 1



    opcao = str(input('Deseja cadastrar mais usuários (S/ N): '))

    opcao = opcao.upper()

    if opcao == 'N':

        print('Maiores de 18 : {}'.format(cont_idade))

        print('Homens cadastrados: {}'.format(cont_M))

        print('Mulheres com menos de 20: {}'.format(cont_IF))

        break