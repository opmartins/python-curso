pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

#print(f'O {pessoas["nome"]}, tem {pessoas["idade"]} anos.')

#print(pessoas.keys())
#print(pessoas.items())

for key in pessoas.keys():
    print(key)


for key, value in pessoas.items():
    print(f'{key} = {value}')