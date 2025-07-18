"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

print(19 * "-=")
print("*** Interpolação básica de strings ***")
print(19 * "-=")
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel + "\n")



print(10 * "-=")
print("*** Com o Format ***")
print(10 * "-=")

nome = 'Sergio'
preco = 99.9322222222
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
print("O {} comprou um carro por R${:5.2f}" .format(nome, preco) + "\n")

# print('O hexadecimal de %d é %08X' % (1500, 1500))