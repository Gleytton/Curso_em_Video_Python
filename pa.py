ptermo = int(input('Digite o primeiro termo da PA: '))

razao = int(input("Digite a razao da PA:"))

for i in range (1,11,1):

	resultado = ptermo + (i - 1)*razao
	print(resultado)