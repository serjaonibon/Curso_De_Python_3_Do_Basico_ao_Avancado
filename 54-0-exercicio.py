"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# try:
#     # Solicita a entrada do usuário
#     entrada_do_usuario = input("Digite um número inteiro: ")
    
#     # Tenta converter a entrada para um número inteiro
#     numero = int(entrada_do_usuario)
    
#     # Se a conversão for bem-sucedida, verifica se o número é par ou ímpar
#     if numero % 2 == 0:
#         print(f"O número {numero} é par.")
#     else:
#         print(f"O número {numero} é ímpar.")

# except ValueError:
#     # Se a conversão falhar (o que acontece se não for um número inteiro),
#     # o programa executa este bloco.
#     print("Entrada inválida! Você não digitou um número inteiro.")

entrada_do_usuario = input("Informe um número inteiro: ")
try:
    numero = int(entrada_do_usuario)
    
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

except ValueError:
    print("Entrada inválida! Você não digitou um número inteiro.")        






