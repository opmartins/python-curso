lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

for cont in range(0,len(lanche)):
    print(lanche[cont])

print('-*' * 10)

for comida in lanche:
    print(comida)

print('-*' * 10)

for pos, comida in enumerate(lanche):
    print(f'Vocu comer {comida}, na posição {pos}')

print(lanche.index('Suco'))
