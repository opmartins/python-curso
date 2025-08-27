soma = 0
contador = 0
for i in range(1,7):
    num = int(input(f'Digite um valor {i}: '))
    if (num % 2) == 0:
        soma += num
        contador += 1
if contador == 1:
    print(f'Você informou {contador} número par. A soma dele é {soma}.')
else:
    print(f'Você informou {contador} números pares. A soma deles é {soma}.')