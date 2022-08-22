print('''TABUADA 2.0

	DIGITE UM NUMERO PARA SABER SUA TABUADA: ''')

num = int(input())

print('A tabuada de {} '.format(num))

for i in range (1,10 + 1,1):

	print('{} x {} = {}'.format(num, i, num*i))