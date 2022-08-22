def maior (*num):
    pos = 0
    maiorValor = - 9999

    while(pos < len(num)):

        if(num[pos]> maiorValor):

            maiorValor = num[pos]
        pos += 1

    print(maiorValor)

maior(2,7,10,25,37,45,-20)