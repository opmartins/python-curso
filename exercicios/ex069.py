
tot18 = totH = totM20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).strip().upper()
    if sexo not in 'FM':
        sexo = str(input('Digite o sexo: ')).strip().upper()
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp=' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print(f'O total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'Temos {totM20} mulheres com menos de 20 anos.')