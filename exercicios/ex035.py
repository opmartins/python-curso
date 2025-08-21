a = float(input('Digite o primeiro segmento de reta: '))
b = float(input('Digite o segundo segmento de reta: '))
c = float(input('Digite o terceiro segmento de reta '))

if a < (b + c) and b < (c +a ) and c < (a + b):
    print('Forma-se um triângulo.')
else:
    print('Não forma-se um triângulo.')

