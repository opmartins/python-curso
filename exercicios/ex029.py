velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Voce foi multado em R$ {:.2f}, por excesso de velocidade.'.format((velocidade-80)*7))
else:
    print('Siga viagem.')

print('Fim do programa.')