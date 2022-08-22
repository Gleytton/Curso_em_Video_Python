import random

num1 = random.randint(0,5)

print('Tente adivinhar qual número o computador escolheu!!!')
num2 = int(input('Digite um numero de 0 a 5: '))

if(num1 == num2):
    print('Parabéns!Você acertou!')
else:
    print('Você errou! Tente novamente!')
    print('O número escolhido foi: {}'.format(num1))