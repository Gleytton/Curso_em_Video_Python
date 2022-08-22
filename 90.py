aluno = dict()

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = int(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 6:

    aluno['situacao'] = 'Aprovado'

else:

    aluno['situacao'] = 'Reprovado'

print(aluno.items())