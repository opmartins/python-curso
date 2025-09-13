aberto = 0
fechado = 0

expressao = str(input('Digite a expressão: '))
lista = list(expressao)

for i in expressao:
    if i == '(':
        aberto += 1
    elif i == ')':
        fechado += 1

if aberto == fechado:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
