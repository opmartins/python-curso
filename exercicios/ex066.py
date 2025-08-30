
soma = cont = 0
while True:
    numero = int(input('Digite o número (999 para): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
    
print(f'Você digitou {cont} números e a soma deles é {soma}.')
