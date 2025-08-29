from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
laco = True

while laco == True:
    opcao = int(input('''
        [1] somar
        [2] multiplicar
        [3] maior número
        [4] novos números
        [5] sair do programa
        
        '''))
    if opcao == 1:
        print(f'O resultado de {n1} + {n2} é: {n1 + n2}')
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é: {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior número é: {n1}')
        else:
            print(f'Entre {n1} e {n2}, o maior número é: {n2}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Fim do programa! Volte sempre!')
        laco = False
    else:
        print('Entrada inválida, tende de novo.')
    sleep(2)

