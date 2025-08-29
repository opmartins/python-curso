
soma_idade = 0
media_idade = 0
maioriadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print(f'------ {p}a pessoa ------')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: '))
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maioriadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioriadehomem:
        maioriadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos')    
print(f'O homem mais velho tem {maioriadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
