n1 = float(input('Digite a nota 1: '))

n2 = float(input('Digite a nota 2: '))

media = (n1 + n2)/2

print('Média: {}'.format(media))

print('Situação do aluno:')

if(media < 5):

    print('Aluno REPROVADO')

elif(media > 5 and media < 6.9):

    print('Aluno em RECUPERACAO')

elif(media > 7):

    print('Aluno APROVADO')

