def fatorial(a, opc = True):

    fat  = 1

    if a == 1 or a == 0:

        if opc == True :

            return 1

        elif  a  == 1 and opc == False :

            msg = " 1! = 1"

            return msg

        elif a == 0 and opc == False:

            msg = ("0! = 1")

            return msg

    elif a != 0 and a != 1:

        for i in range (1, a + 1):

            fat *= i

        if  opc == True:

            msg = str(a) + '! =' + str(fat)
            return msg

        else:

            for j in range(a,1,-1):

                print(f'{j} x ', end ='' )

            print(f'1 = ', end='' )

            return fat



# programa principal

print(fatorial(4,False))



