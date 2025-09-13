lista = []

for i in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {i}: ')))

print(f'O maior valor digitado foi {max(lista)}.')
print(f'O menor valor digitado foi {min(lista)}.')

print(f'O maior valor digitado ({max(lista)}) está na posição: ', end='')
for indice, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{indice}...', end='')
    
print()

print(f'O menor valor digitado ({min(lista)}) está na posição: ', end='')
for indice, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{indice}...', end='')
