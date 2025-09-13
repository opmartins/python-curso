lista = ['Hamburger', 'Suco', 'Pizza', 'Picolé']


# ADICIONAR VALORES EM LISTAS

lista.append('Cookie') #Adiciona items ao final da lista
print(lista)

print('=-' * 15)

lista.insert(1, 'Cachorro Quente') #Adiciona um item na posição de indice especificada
print(lista)

print('=-' * 15)

# REMOVER VALORES EM LISTAS

del lista[1] #Deleta o item do índice especificado
lista.pop(1) #Deleta o último valor da lista (se não passar parâmetro) ou deleta o valor no índice especificado
lista.remove('Pizza') #Deleta o valor na lista, por nome

if 'Pizza' in lista:  #REMOÇÃO CONDICIONAL - Ao tentar remover um valor que não está na lista dá erro. Por isso podemos fazer uma verificação antes de remover o valor.
    lista.remove('Pizza')


# CRIAR LISTA A PARTIR DO range()

nova_lista = list(range(4,11))

print(nova_lista)


# COLOCAR ITEMS EM ORDEM

nova_lista.sort(reverse=True) #Organiza os valores da lista em ordem, se for enviado sem parâmetro. Com o parâmetro ele organiza do contrário

# Descobrir quantos elementos tem a lista

len(nova_lista)

# Mostrar o valor junto com o íncice

for indice, valor in enumerate(nova_lista):
    print(f'Na posição {indice} encontrei o valor {valor}.')


# Colocar valores dentro da lista com entrada do teclado
valores = []
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)