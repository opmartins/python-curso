

while True:
    numero = int(input('Digite o número para ver sua tabuada: '))
    if numero > 0:
        for i in range (1,11):
            print(f'{numero} x {i} = {numero * i}')
    else:
        break
