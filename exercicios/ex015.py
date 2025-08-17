dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados?'))

total = (dia*60)+(km*0.15)

print('O valor a ser pago é de {:.2f}'.format(total))