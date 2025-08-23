from datetime import datetime

ano = int(input('Digite seu ano de nascimento: '))

ano_atual = datetime.now().year
idade = (ano_atual - ano)

if (idade < 18):
    diferenca = 18 - idade 
    print(f'Ainda não é o momento de se alistar. Você deverá se alistar em {diferenca} ano(s) ({ano+18}).') 
elif idade > 18:
    diferenca = idade - 18
    print(f'Já passou do momento de se alistar. Você deveria ter se alistado {diferenca} anos atrás ({ano+18}).')
elif idade == 18:
    print('Você tem que alistar imediatamente.')