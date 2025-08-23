a = float(input('Digite o primeiro segmento de reta: '))
b = float(input('Digite o segundo segmento de reta: '))
c = float(input('Digite o terceiro segmento de reta '))

if a < (b + c) and b < (c +a) and c < (a + b):
    print('Forma-se um triângulo.')
    if a == b == c:
        print('O triângulo é equilátero.')
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Não forma-se um triângulo.')



