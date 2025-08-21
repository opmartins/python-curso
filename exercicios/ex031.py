distancia = float (input('Digite a distância da viagem: '))

if distancia >= 200:
    print('O preço da viagem é {:.2f}'.format(distancia*0.45))
else:
    print('O preço da viagem é {:.2f}'.format(distancia*0.5))