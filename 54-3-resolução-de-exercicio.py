from itertools import count


nome = input("Digite seu nome: ")
carateres = (len(nome))

# if len(nome) > 0 and len(nome) <= 4:
#     print(f'{nome}, seu nome possui {carateres} letras! Por isso é curto')
# elif len(nome) <= 6:
#     print(f'{nome}, seu nome possui {carateres} letras! Por isso normal')
# elif len(nome) <= 0 and nome == ' ':
#     print('A entrada foi digitada ERRADA, tente novamente')
# else:
#     print(f'{nome}, seu nome possui {carateres} letras! Por isso grande')

if carateres < 1:
    print('A entrada foi digitada ERRADA, tente novamente!')
elif carateres <= 4:
    print(f'{nome}, seu nome possui {carateres} letra(s)! Por isso é curto!')
elif carateres <= 6:
    print(f'{nome}, seu nome possui {carateres} letra(s)! Por isso é normal!')
else:
    print(f'{nome}, seu nome possui {carateres} letra(s)! Por isso é grande!')
