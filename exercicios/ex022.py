nome = str(input('Digite seu nome: ')).strip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras.'.format(len(nome.replace(' ', ''))))

separado = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras'.format(separado[0], len(separado[0])))