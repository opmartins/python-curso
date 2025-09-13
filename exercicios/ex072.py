contagem_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                     'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                         'dezessete', 'dezoito', 'dezenove', 'vinte')

resposta = 'S'

while resposta in 'Ss':
    while True:
        numero = int(input('Digite um número de 0 a 20: '))
        if 0 <= numero <= 20:
            break
    print(f'O número digitado por extenso é {contagem_extenso[numero]}.')
    resposta = str(input('Deseja continuar? ')).strip().upper()
    if resposta == 'N':
        break
        