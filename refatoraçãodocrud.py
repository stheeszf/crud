# Sistema para registro de Atividades Físicas

nomes = []
tipos = []
distancias = []
duracoes = []
ativa = []


def cadastrar(nomes, tipos, distancias, duracoes, ativa):
    nome = input("Nome da atividade: ")
    tipo = input("Tipo de atividade: ")

    try:
        distancia = float(input("Distância em km: "))
        duracao = int(input("Duração em minutos: "))
    except ValueError:
        print("Digite valores numéricos válidos.")
        return

    if nome == "" or tipo == "" or distancia <= 0 or duracao <= 0:
        print("Dados inválidos. Preencha tudo e use valores maiores que zero.")
    else:
        nomes.append(nome)
        tipos.append(tipo)
        distancias.append(distancia)
        duracoes.append(duracao)
        ativa.append(True)

        print("Atividade cadastrada com sucesso!")


def listar(nomes, tipos, distancias, duracoes, ativa):
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


def buscar(nomes, tipos, distancias, duracoes, ativa):
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


def alterar(nomes, tipos, distancias, duracoes, ativa):
    try:
        n = int(input("Número da atividade a editar: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if n >= 1 and n <= len(nomes):
        if ativa[n - 1] == True:
            nome = input("Novo nome: ")
            tipo = input("Novo tipo: ")

            try:
                distancia = float(input("Nova distância em km: "))
                duracao = int(input("Nova duração em minutos: "))
            except ValueError:
                print("Digite valores numéricos válidos.")
                return

            if nome == "" or tipo == "" or distancia <= 0 or duracao <= 0:
                print("Dados inválidos. A atividade não foi alterada.")
            else:
                nomes[n - 1] = nome
                tipos[n - 1] = tipo
                distancias[n - 1] = distancia
                duracoes[n - 1] = duracao

                print("Atividade editada com sucesso!")

        else:
            print("Essa atividade já foi excluída.")

    else:
        print("Número fora da lista.")


def excluir(nomes, ativa):
    try:
        n = int(input("Número da atividade a excluir: "))
    except ValueError:
        print("Digite um número válido.")
        return

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


def menu(nomes, tipos, distancias, duracoes, ativa):
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
            cadastrar(nomes, tipos, distancias, duracoes, ativa)

        elif opcao == "2":
            listar(nomes, tipos, distancias, duracoes, ativa)

        elif opcao == "3":
            buscar(nomes, tipos, distancias, duracoes, ativa)

        elif opcao == "4":
            alterar(nomes, tipos, distancias, duracoes, ativa)

        elif opcao == "5":
            excluir(nomes, ativa)

        elif opcao == "6":
            print("Encerrando o Strava")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu(nomes, tipos, distancias, duracoes, ativa)