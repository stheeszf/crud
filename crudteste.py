print("STRAVA")
atividade = ""
distancia = 0.0
duracao = 0
tipo = ""
cadastrada = False

while True:
    print("MENU PRINCIPAL")
    print("1. Cadastrar atividades")
    print("2. Listar atividades")
    print("3. Editar atividades")
    print("4. Excluir atividades")
    print("5. Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        if cadastrada == False:
            atividade = input("Nome da atividade")
            tipo = input("Tipo de atividade:")
            distancia = float(input("Distância em km:"))
            duracao = int(input("Duração em minutos:"))

            cadastrada = True

            print("Atividade cadastrada com sucesso")
        else:
            print("Já existe uma atividade cadastrada")

    elif opcao == "2":
        if cadastrada == True:
            print("ATIVIDADE CADASTRADA")
            print("Nome: ", atividade)
            print("Tipo: ", tipo)
            print("Distância: ", distancia, "km")
            print("Duração: ", duracao, "minutos")
        else:
            print("Nenhuma atividade cadastrada.")

    elif opcao == "3":
        if cadastrada == True:
            print("EDITAR ATIVIDADE")
            atividade = input("Novo nome da atividade:")
            tipo = input("Novo tipo: ")
            distancia = float(input("Nova distância em km: "))
            duracao = int(input("Nova duração em minutos: "))

            print("Atividade editada com sucesso!")
        else:
            print("Nenhuma atividade para editar")

    elif opcao == "4":
        if cadastrada == True:
            confirmacao = input("Deseja excluir a atividade?(Sim/Não) ")

            if confirmacao == "Sim":
                atividade = ""
                tipo = ""
                distancia = 0.0
                duracao = 0
                cadastrada = False

                print("Atividade excluída com sucesso.")
            else:
                print("Exclusão cancelada.")
        else:
            print("Nenhuma atividade para excluir.")

    elif opcao == "5":
        print("Encerrando o Strava")
        break

    else:
        print("Opção inválida. Tente novamente.")