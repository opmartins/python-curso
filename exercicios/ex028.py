from random import randint
from time import sleep

sorteado = randint(0,5)

numero = int(input('Tente adivinhar o número entre 0 e 5!'))

print('Processando...')
sleep(1)

if numero == sorteado:
    print('Parabéns, você acertou o número {}.'.format(sorteado))
else:
    print('O número {} está incorreto. O número sorteado era {}.'.format(numero,sorteado))