from random import choice
from time import sleep
from sys import exit

items = ('Pedra', 'Papel', 'Tesoura')

escolhido = choice(items)

jogador = int(input("""
          Escolha uma opção:
          
          [1] Pedra
          [2] Papel
          [3] Tesoura
          
          """))

if jogador == 1:
    jogador = 'Pedra'
elif jogador == 2:
    jogador = 'Papel'
elif jogador == 3:
    jogador = 'Tesoura'
else:
    print('Opção inválida.')
    exit()

print(f"""
      
      Você escolheu {jogador}!!
      
      """)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('')

if jogador == 'Pedra' and escolhido == 'Pedra':
    print(f'Empate! O computador escolheu {escolhido}!')
elif jogador == 'Pedra' and escolhido == 'Papel':
    print(f'Perdeu! O computador escolheu {escolhido}!')
elif jogador == 'Pedra' and escolhido == 'Tesoura':
    print(f'Venceu! O computador escolheu {escolhido}!')

if jogador == 'Papel' and escolhido == 'Pedra':
    print(f'Venceu! O computador escolheu {escolhido}!')
elif jogador == 'Papel' and escolhido == 'Papel':
    print(f'Empate! O computador escolheu {escolhido}!')    
elif jogador == 'Papel' and escolhido == 'Tesoura':
    print(f'Perdeu! O computador escolheu {escolhido}!')

if jogador == 'Tesoura' and escolhido == 'Pedra':
    print(f'Perdeu! O computador escolheu {escolhido}!')
elif jogador == 'Tesoura' and escolhido == 'Papel':
    print(f'Venceu! O computador escolheu {escolhido}!')
elif jogador == 'Tesoura' and escolhido == 'Tesoura':
    print(f'Empate! O computador escolheu {escolhido}!')

