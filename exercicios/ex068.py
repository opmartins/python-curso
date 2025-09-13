from random import randint
v = 0 
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v +=1
        else:
            print('Você perdeu!')