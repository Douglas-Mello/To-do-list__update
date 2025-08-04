pessoa = dict()
tarefas = list()

def lista(opc):
    match opc:
        case 1:
            with open("ListadeTarefa.txt", 'a+') as file:
                file.seek(0)
                linhas = file.readlines()
                nome = input('Nome da pessoa: ').strip()
                for linha in linhas:
                    if f"Nome {nome}" in linha:
                        return 'Essa pessoa já foi cadastrada'
                tarefa = input(f"Digite a primeira tarefa de {nome}: ").strip()
                pessoa[nome] = [tarefa]
                file.write(f"Nome {nome} Tarefas: {len(pessoa[nome])} --> {pessoa[nome]}\n")

        case 2:
            print("Quer adicionar tarefa a quem:")
            with open("ListadeTarefa.txt", "r") as f:
                linhas = f.readlines()
                for linha in linhas:
                    print(linha.split('Tarefas')[0].split('Nome')[1].strip())

            nome = input("Sua escolha: ").strip()

            for linha in linhas:
                if f"Nome {nome}" in linha:
                    tarefasAntigas = linha.split('-->')[1].strip()
                    tarefasAntigas = tarefasAntigas.replace('[', '').replace(']', '').replace("'", "")

                    tarefasLista = tarefasAntigas.split(',')
                    tarefas = []
                    for t in tarefasLista:
                        t_limpa = t.strip()
                        if t_limpa:
                            tarefas.append(t_limpa)

                    pessoa[nome] = tarefas[:]
                    break
            else:
                return "Pessoa não encontrada."

            while True:
                nova = input("Tarefa a ser adicionada: ").strip()
                pessoa[nome].append(nova)
                cont = input("Quer adicionar mais tarefas [s/n]: ").strip().lower()
                if cont == 'n':
                    with open("ListadeTarefa.txt", "w") as f:
                        for linha in linhas:
                            if f"Nome {nome}" in linha:
                                f.write(f"Nome {nome} Tarefas: {len(pessoa[nome])} --> {pessoa[nome]}\n")
                            else:
                                f.write(linha)
                    break

        case 3:
            with open("ListadeTarefa.txt", "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    print(linha.split('Tarefas')[0].split('Nome')[1].strip())

            nome = input("Quer ver tarefa de quem: ").strip()
            for linha in linhas:
                if f"Nome {nome}" in linha:
                    tarefa = linha.split('-->')[1].strip()
                    tarefa = tarefa.strip("[]").replace("'", "")
                    mostrar = tarefa.split(',')
                    mostrar_limpo = []
                    for t in mostrar:
                        t_limpa = t.strip()
                        if t_limpa:
                            mostrar_limpo.append(t_limpa)
                    mostrar = mostrar_limpo
                    for t in mostrar:
                        print(f"- {t}")
                    break
            else:
                print('Pessoa não encontrada')

        case 4:
            with open("ListadeTarefa.txt", "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    print(linha.split('Tarefas')[0].split('Nome')[1].strip())

            nome = input("Quer remover a tarefa de quem: ").strip()

            for linha in linhas:
                if f"Nome {nome}" in linha:
                    tarefa = linha.split('-->')[1].strip()
                    tarefa = tarefa.strip("[]").replace("'", "")
                    mostrar = tarefa.split(',')
                    mostrar_limpo = []
                    for t in mostrar:
                        t_limpa = t.strip()
                        if t_limpa:
                            mostrar_limpo.append(t_limpa)
                    mostrar = mostrar_limpo
                    print("Tarefas atuais:")
                    for t in mostrar:
                        print(f"- {t}")
                    break
            else:
                print("Pessoa não encontrada.")
                return

            excluir = input("Qual tarefa deseja excluir: ").strip()
            if excluir in mostrar:
                mostrar.remove(excluir)
                with open("ListadeTarefa.txt", "w") as file:
                    for linha in linhas:
                        if nome in linha:
                            file.write(f"Nome {nome} Tarefas: {len(mostrar)} --> {mostrar}\n")
                        else:
                            file.write(linha)
                print("Tarefa removida com sucesso.")
            else:
                print("Tarefa não encontrada.")
