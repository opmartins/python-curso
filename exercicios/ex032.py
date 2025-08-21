import datetime

ano = int(input('Digite o ano a ser verificado (Digite 0 para o ano atual): '))

if ano == 0:
    ano = datetime.datetime.now()
    ano = ano.year
    
print('O ano atual é {}'.format(ano))    
    
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('O ano é bissexto.')
else:
        print('O ano não é bissexto.')




