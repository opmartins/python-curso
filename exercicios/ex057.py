sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Digite o sexo [M/F]: ')).upper().strip()
print('Dados registrados com sucesso.')