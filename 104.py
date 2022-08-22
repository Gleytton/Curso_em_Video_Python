
def leiaInt(num):

    if(num.isnumeric() == False):

        print('\033[0;31; mO valor digitado não é um numero')

    else:

        print(f'{num} é um número')



n = str(input('Digite um número: '))
leiaInt(n)