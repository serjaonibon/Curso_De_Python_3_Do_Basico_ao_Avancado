
# hora = input("Informe a hora (0-23): ")
# minuto = input("Informe os minutos (0-59): ")
# try:
#     hora = int(hora)
#     minuto = int(minuto)

#     if 0 <= hora < 24 and 0 <= minuto < 60:
#         if hora < 12:
#             print("Bom dia!")
#         elif hora < 18:
#             print("Boa tarde!")
#         else:
#             print("Boa noite!")
#     # else:
#     #     print("Hora ou minuto inválido!")
# except ValueError:
#     print("Entrada inválida! Você não digitou números válidos para hora e minuto.")


hora = input('Informe a hora? ')
minuto = input('Informe os minutos? ')


try:
    horario = int(hora)
    minutos = int(minuto)
    if horario <= 11 and minutos <= 59:
        print("Bom dia!")
    elif horario < 18 and minutos <= 59:
        print("Boa tarde!")
    else:
        print("Boa noite!")
except ValueError:
    print("Entrada inválida! Você não digitou números válidos para hora e minuto.")            
