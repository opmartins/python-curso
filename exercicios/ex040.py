n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print(f'Sua média foi {m:.2f}. Você está REPROVADO.')
elif 5 <= m <= 6.9:
    print(f'Sua média foi {m:.2f}. Você está de RECUPERAÇÃO.')
else:
    print(f'Sua média foi {m:.2f}. Você está APROVADO.')
