def area(lar,comp):

    a = lar * comp

    print("A área do terreno de {} x {} será: {}".format(lar,comp, a))



lar = float(input("Digite a largura do terreno: "))

comp = float(input("Digite o comprimento do terreno: "))

area(lar, comp)