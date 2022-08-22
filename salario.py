salario = float(input('Digite o salario: R$'))

aumento = 0
if(salario > 1250):

     aumento = salario*0.10

else:

    aumento = salario * 0.15

print('O aumento do salário de {} foi de: {}'.format(salario, aumento))
print('O novo salário é de: {}'.format(salario +  aumento))