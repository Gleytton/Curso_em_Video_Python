maior = 0.00

menor = 1000000.00

for i in range(1,6,1):
	peso = float(input('Digite o peso da {} pessoa: '.format(i)))

	if peso > maior:

		maior = peso

	if peso < menor:

		menor = peso

print('Maior peso: {}' .format(maior))
print('Menor peso: {}' .format(menor))
