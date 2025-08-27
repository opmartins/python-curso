from datetime import datetime
ano_atual = datetime.now().year
#ano_atual = ano_atual.year
anos = []
cont_maior = 0
cont_menor = 0

for i in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {i}a pessoa: '))
    anos.append(ano)

for ano in anos:
    idade = ano_atual - ano
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'São {cont_maior} pessoas maiores de idade e {cont_menor} pessoas menores de idade.')