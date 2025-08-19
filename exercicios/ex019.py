from random import choice

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do terceiro aluno: ')

lista = [a,b,c,d]

sorteado = choice(lista)

print('O aluno escolhido é {}'.format(sorteado))