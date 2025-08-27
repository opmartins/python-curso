num = int(input('Digite o número: '))

cont = 0
for i in range (1,num+1):
    if num % i == 0:
        cont += 1
if cont == 2:
    print('Número primo.')
else:
    print('Numero não primo.')
