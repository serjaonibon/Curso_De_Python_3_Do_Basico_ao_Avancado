"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
# 0 1 2 3 4 5 6 7 -> Índices
#-8-7-6-5-4-3-2-1 -> Índices regressivos
# o l á m u n d o -> String
variavel = 'Olámundo'
print(variavel[::-1] + "\n")
print(variavel[0] + "\n" + "")
print(variavel[-2],"-2", "\n")
print(variavel[-8], "-8", "\n")
print(variavel[3],"3", "\n")
print(variavel[0:8:2] + "\n")
print(len(variavel), "\n")