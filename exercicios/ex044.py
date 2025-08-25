
preco = float(input('Preço das compras: '))

print("""
      
      Formas de pagamento:
      
      [ 1 ] à vista em dinheiro / cheque
      [ 2 ] à vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão
      
      """)

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    preco -= preco * 0.10
    print(f'O valor da compra é de {preco}, com 10% de deconto.')
elif opcao == 2:
    preco -= preco * 0.05
    print(f'O valor da compra é de {preco}, com 5% de desconto.')
elif opcao == 3:
    print(f'O valor da compra é de {preco}.')
elif opcao == 4:
    preco += preco * 0.2
    print(f'O valor da compra é de {preco}, com 20% de júros.')
    
else:
    print('Opção inválida.')