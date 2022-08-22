while True:

    num = int(input('Digite o valor da tabuada: '))

    if num < 0:

        break

    for i in range(1,11):

        mul = num * i

        print('{} x {} = {}'.format(num, i, mul))

