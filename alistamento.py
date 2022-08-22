nasc = int(input('Digite o ano de nascimento: '))
from datetime import datetime

data = datetime.now()

if( data.year - nasc < 18 ):
    print('Ainda vai se alistar')
    print('Faltam {} anos para o seu alistamento'.format(18 -(data.year - nasc)))
elif(data.year - nasc > 18):
    print('Já passou da hora de se alistar')
    print('Você deveria ter se alistado a {} anos'.format((data.year - nasc) - 18))
elif(data.year - nasc == 18):
    print('Esta na hora de se alistar')