n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'Primeiro valor maior: O número {n1} é maior que {n2}.')
elif n2 > n1:
    print(f'Segundo valor maior: O número {n2} é maior que {n1}.')
else:
    print(f'Os números são iguais.')
