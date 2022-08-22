from datetime import datetime

ano_atual = datetime.now()


for i in range (0,7,1):

	ano = int(input('Digite o ano de nascimento: '))

	
	if ( ano_atual.year - ano >= 18):

		print( 'Maior de idade')

	else:

		print( 'Menor de idade')