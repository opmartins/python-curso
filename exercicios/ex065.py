
validacao = 's'
soma = 0
cont = 0
maior = menor = 0


while validacao in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    validacao = str(input('Deseja continuar? ')).upper().strip()

print(f'Você digitou {cont} números. A média é {soma/cont}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')