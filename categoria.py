from datetime import datetime

date = datetime.now()

anoAtual = date.year

nasc = int(input('Digite o ano de nascimento: '))


if( anoAtual - nasc < 10 ):

    print('Categoria: MIRIM')

elif( anoAtual - nasc >= 10 and anoAtual - nasc < 15 ):

    print('Categoria: INFANTIL')

elif( anoAtual - nasc >= 15 and anoAtual - nasc < 19):

    print('Categoria: JUNIOR')

else:

    print(' Categoria: SENIOR')

