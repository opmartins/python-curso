valores = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))

print(f'Você digitou os valores {valores}.')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1} posição')
else:
    print('Não houve valor 3 digitado.')

cont = 0
for n in valores:
    if n % 2 == 0:
        print(n)
        cont += 1

print(f'São {cont} números pares.')