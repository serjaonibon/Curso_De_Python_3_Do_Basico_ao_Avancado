entrada_do_usuario = input("Informe um número inteiro: ")
try:
    numero = int(entrada_do_usuario)
    
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

except ValueError:
    print("Entrada inválida! Você não digitou um número inteiro.")    