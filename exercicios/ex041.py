from datetime import datetime

ano = int(input('Digite o ano de nascimento do atleta:'))

ano_atual = datetime.now().year
idade = (ano_atual - ano)

print(f'A idade do atleta é {idade}.')

if idade <= 9:
    print('MIRIM')
elif 14 >= idade > 9:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SENIOR')
else:
    print('MASTER')