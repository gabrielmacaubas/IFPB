from math import sqrt

a = int(input('digite o coeficiente "a" da equacao de 2º grau: '))
b = int(input('digite o coeficiente "b" da equacao de 2º grau: '))
c = int(input('digite o coeficiente "c" da equacao de 2º grau: '))

delta = b**2 - (4 * a * c)

if delta >= 0:
    raiz_x1 = (-b + sqrt(delta)) / (2 * a)
    raiz_x2 = (-b - sqrt(delta)) / (2 * a)
    print(raiz_x1, raiz_x2)

else:
    print("Nao existem as raizes da equacao.")
