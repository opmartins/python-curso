a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

lista = [a,b,c]

maior_valor = max(lista)
menor_valor = min(lista)

print('O maior valor é {} e o menor valor é {}.'.format(maior_valor, menor_valor))