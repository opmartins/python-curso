salario = float(input('Digite o salário: '))

if salario > 1250:
    salario += salario * 0.1
else:
    salario += salario * 0.15

print('O salário com aumento será {}'.format(salario))