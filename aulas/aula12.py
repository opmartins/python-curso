nome = str(input('Qual é seu nome? '))

if nome == 'Otavio':
    print('Que nome lindo!!')
elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Cláudia Ana Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal! kkkk')
    
    
print('Tenha um bom dia {}!'.format(nome))