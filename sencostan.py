import math

angulo = float(input("Digite o valor de um angulo (em radianos): "))

radiano = math.radians(angulo)

print(radiano)

print('sin({}) = {}'.format(angulo,math.sin(radiano)))
print('cos({}) = {}'.format(angulo,math.cos(radiano)))
print('tan({}) = {}'.format(angulo,math.tan(radiano)))
