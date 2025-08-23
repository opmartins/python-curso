casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
anos = int(input('Digite em quantos anos vai pagar: '))

prestacao = casa / (anos * 12)

print('A prestação será de {:.2f} por mês'.format(prestacao))

if prestacao > (salario * 0.3):
    print('Emprestimo negado')
else:
    print('Emprestimo aceito.')