# Sistema para registro de Atividades Físicas

# uma lista para cada dado; a posição i de cada lista pertence à mesma atividade
nomes = []
tipos = []
distancias = []
duracoes = []
# ativa[i] é True enquanto a atividade existe; ao excluir, vira False
ativa = []

while True:
    print("MENU PRINCIPAL")
    print("1. Cadastrar atividade")
    print("2. Listar atividades")
    print("3. Buscar atividade")
    print("4. Editar atividade")
    print("5. Excluir atividade")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da atividade: ")
        tipo = input("Tipo da atividade: ")
        distancia = float(input("Distância em km: "))
        duracao = int(input("Duração em minutos: "))

        if nome == "" or tipo == "" or distancia <= 0 or duracao <= 0:
            print("Dados inválidos. Preencha tudo e use valores maiores que zero.")
        else:
            nomes.append(nome)
            tipos.append(tipo)
            distancias.append(distancia)
            duracoes.append(duracao)
            ativa.append(True)
            print("Atividade cadastrada com sucesso!")

    elif opcao == "2":
        achou = False
        i = 0
        while i < len(nomes):
            if ativa[i] == True:
                if achou == False:
                    print("ATIVIDADES CADASTRADAS")
                print(i + 1, "-", nomes[i], "|", tipos[i], "|",
                      distancias[i], "km |", duracoes[i], "min")
                achou = True
            i = i + 1
        if achou == False:
            print("Nenhuma atividade cadastrada.")

    elif opcao == "3":
        termo = input("Buscar por nome ou tipo: ")
        achou = False
        i = 0
        while i < len(nomes):
            if ativa[i] == True:
                if termo == nomes[i] or termo == tipos[i]:
                    print(i + 1, "-", nomes[i], "|", tipos[i], "|",
                          distancias[i], "km |", duracoes[i], "min")
                    achou = True
            i = i + 1
        if achou == False:
            print("Nenhuma atividade encontrada.")

    elif opcao == "4":
        n = int(input("Número da atividade a editar: "))
        if n >= 1 and n <= len(nomes):
            if ativa[n - 1] == True:
                nomes[n - 1] = input("Novo nome: ")
                tipos[n - 1] = input("Novo tipo: ")
                distancias[n - 1] = float(input("Nova distância em km: "))
                duracoes[n - 1] = int(input("Nova duração em minutos: "))
                print("Atividade editada com sucesso!")
            else:
                print("Essa atividade já foi excluída.")
        else:
            print("Número fora da lista.")

    elif opcao == "5":
        n = int(input("Número da atividade a excluir: "))
        if n >= 1 and n <= len(nomes):
            if ativa[n - 1] == True:
                confirmacao = input("Deseja excluir a atividade? (Sim/Não) ")
                if confirmacao == "Sim":
                    ativa[n - 1] = False
                    print("Atividade excluída com sucesso.")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Essa atividade já foi excluída.")
        else:
            print("Número fora da lista.")

    elif opcao == "6":
        print("Encerrando o Strava")
        break

    else:
        print("Opção inválida. Tente novamente.")