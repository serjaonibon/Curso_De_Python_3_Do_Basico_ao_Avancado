dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

print(f'O total em segundos será: {dias * 86400 + horas *3600 + minutos * 60 + segundos}')
