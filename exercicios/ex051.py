termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao

for i in range(termo,decimo + razao,razao):
    print(f'{i}', end=' -> ')

print('ACABOU')