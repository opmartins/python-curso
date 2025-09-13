princ = []
temp = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()



    while True:
        continuar = str(input('Deseja continuar? ')).strip().upper()
        if continuar in 'SN':
            break
        else:
            print('Digite uma opção válida.')
    if continuar == 'N':
        break
print('-=' * 30)

print(f'Ao todo foram {len(princ)} pessoas cadastradas.')        
print(f'O maior peso foi de {maior} Kg.')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor} Kg.')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')