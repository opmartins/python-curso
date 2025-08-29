from random import randint

computador = randint(0,10)
tentativas = 1

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual seu palpite? '))

while jogador != computador:
    if jogador > computador:
        print('Menos, tente mais uma vez.')
        jogador = int(input('Qual seu palpite? '))
        tentativas += 1
    elif jogador < computador:
        print('Mais, tente mais uma vez.')
        jogador = int(input('Qual seu palpite? '))
        tentativas += 1

print(f'Acertou em {tentativas}! Parabéns!')