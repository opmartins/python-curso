
flag = cont = soma = 0

while flag != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:    
        soma += numero
        cont += 1
    elif numero == 999:
        flag = 999


print(f'Você digitou {cont} números e a soma deles é {soma}.')