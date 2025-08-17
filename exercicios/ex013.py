salario = float(input('Digite o salário: '))

aumento = salario * 0.15

novo_salario = salario + aumento

print('Um salário de {:.2f}, com um aumento de {} (15%), fica em {}.'.format(salario,aumento,novo_salario))