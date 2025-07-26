salario = float(input("Digite o salário do funcionário: "))
aumento = float(input("Digite o percentual de aumento: "))
novo_salario = salario + (salario * aumento / 100)

print(f'O novo salário do colaborador será de R$ {novo_salario:.2f} com um aumento de {aumento}%')
