lista = []
for i in range(1,6):
    peso = float(input(f'Digite o {i}o peso: '))
    lista.append(peso)

print(f'O maior peso da lista é {max(lista)}')
print(f'O menor peso da lista é {min(lista)}')
