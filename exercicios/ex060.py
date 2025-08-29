n = int(input('Digite o número para calcular o fatorial: '))
contador = n
f = 1
print(f'Calculando o fatorial de {n}...')

while contador > 0: 
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
    
print(f)