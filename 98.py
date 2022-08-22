import time

def contador(inicio, fim , passo):

    for i in range(inicio, fim, passo):

        print(i, end= " ")
        time.sleep(1)
    print()


contador(1,11,1)

contador(10, 0, -2 )

inicio = int(input("Digite um numero para o iniciar do intervalo: "))

fim = int(input("Digite um numero para o final do intervalo: "))

passo = int(input("Digite um numero de passo:  "))

if (passo >= 0):


    contador(inicio, fim, passo)

else:

    contador(inicio, fim, passo)

if (inicio > fim):

    passo = (-1) * passo
    contador(inicio, fim, passo)
