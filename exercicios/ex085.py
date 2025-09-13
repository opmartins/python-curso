
lista = []
for i in range(0,7):
    lista.append(int(input(f'Digite o {i+1}o valor: ')))

print(f'Os valores pares são ', end='')
for i in lista:
    if i % 2 == 0:
        print(f'{i}...', end='')

print()

print(f'Os valores ímpares são ', end='')
for i in lista:
    if i % 2 == 1:
        print(f'{i}...', end='')