nome = str(input("Por gentileza, digite seu nome? "))
idade = int(input("Por gentileza, digite sua idade: "))
espacos_nome = nome.count(" ")
nome_sem_espacos =  len(nome.strip())

if nome > " "  and idade >= 1 :
    print("'\n'Obrigado por inserir as informações solicitadas!" + "\n"
          "Iremos dar continuidade à nossa atividade!" + "\n")
    print(15 * "-=")
    print(f" Seu nome é: {nome}" + "\n",
    f"Seu nome invertido é {nome[::-1]}" + "\n",
    f"No seu nome, há {espacos_nome} espaço(s) em branco."  + "\n",
    f"Seu nome tem {nome_sem_espacos} letras. " + "\n",
    f"A primeira letra do seu nome é {nome[0]}" + "\n",
    f"A última letra do seu nome é '{nome[-1]}'")
    print(15 * "-=" + "\n")
    
else:
    print("Você não inseriur as informações solicitadas! FIM!")