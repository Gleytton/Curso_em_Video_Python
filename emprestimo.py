val_casa = int(input("Digite o valor da casa: R$ "))
val_sal = int( input("Digite o valor do salário: R$ "))
quantidade = int( input("Digite em quantos anos deseja pagar a casa: 55"))

quantidade = quantidade * 12

prestacao = val_casa / quantidade

if(prestacao <= 0.3 * val_sal):
    print('Emprestimo aprovado')
else:
    print('Emprestimo reprovado')



