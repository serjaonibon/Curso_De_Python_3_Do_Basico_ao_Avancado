preco_mercadoria = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
novo_preco = preco_mercadoria - (preco_mercadoria * desconto / 100)

print(f'O produto receberá um desconto de {desconto:.2f}%, e o novo preço da mercadoria com desconte é R$ {novo_preco:.2f}')