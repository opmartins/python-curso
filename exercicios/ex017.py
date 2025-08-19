from math import sqrt, hypot

a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))

#h = sqrt(a**2+b**2) << Outra forma de fazer
h2 = hypot(a,b)

print('A hipotenusa é {:.2f}'.format(h2))