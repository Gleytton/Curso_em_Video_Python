numero = int(input('Digite numero:'))

cont = 0

for i in range (1,numero + 1,1):
	
	if( numero % i == 0):

		cont += 1



if( cont < 3):

	print("O  número {} é primo" .format(numero))

else:

	print("O número {} não é primo" .format(numero))





