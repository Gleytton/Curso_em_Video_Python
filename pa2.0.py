a1 = int(input('Digite o primeiro termo da PA: '))

razao = int(input('Digite a razão da PA: '))

contador = 1

termo = 0

while contador < 11:

    termo = a1 + (contador - 1)*razao

    print(termo)

    contador += 1