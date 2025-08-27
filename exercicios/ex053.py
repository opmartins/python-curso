frase = str(input('Digite a frase ou palavra: ')).strip().upper()

separado = frase.split()
juntado = ''.join(separado)
invertida= juntado[::-1]



if invertida == juntado:
    print(f'A frase/palavra {frase} é um palíndromo.')
else:
    print(f'A frase/palavra {frase} não é um palíndromo.')
