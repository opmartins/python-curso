lista =[]
cont = 0

while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in lista:
        lista.append(valor)
        cont += 1
    else:
        print(f'O valor {valor} já está na lista. ')
    
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
        else:
            print('Resposta inválida. Somente S ou N. ')
    
    if continuar in 'N':
        break

lista.sort(reverse=True)
print(f'Foram digitados {cont} valores, na lista: {lista}')

if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')