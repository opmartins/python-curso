lista =[]
pares=[]
impares=[]

while True:
    numero = int(input('Digite o Valor: '))
    lista.append(numero)
    continuar = str(input('Deseja continuar?'))
    if continuar in 'Nn':
        break

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)





print(lista)
print(f'Os números pares são: {pares}.')
print(f'Os números ímpares são: {impares}.')