peso = float(input('Digite o peso (kg): '))

altura = float(input('Digite a altura: '))

imc = peso /(altura**2)

if(imc < 18.5):

    print('Abaixo do peso')

elif( imc >= 18.5 and imc < 25):

    print('Peso ideal')

elif( imc >= 25 and imc < 30):

    print('Sobrepeso')

else:

    print('Obesidade morbida')