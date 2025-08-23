numero = int(input('Digite um número inteiro: '))

print("""
Escolha uma das bases para conversão:
      
      [1] converter para binário
      [2] converter para octal
      [3] converter para hexadecimal

      """)

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} em binário é: {}.'.format(numero,bin(numero)))
elif opcao == 2:
    print(f'O número {numero} em octal é: {numero:o}')
elif opcao == 3:
    print(f'O número {numero} em hexadecimal é: {numero:x}')
else:
    print('Opção inválida.')