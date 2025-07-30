pessoa = list()

def lista(opc):
    tarefas= list()
    match opc:
        case 1:
            with open("ListadeTarefa.txt", 'a+') as file:
                nome=input('nome da pessoa: ')
                c=1
                tarefa=input(f"Digite a primeira Tarefa de {nome}: ")
                pessoa.append(nome)
                for p in pessoa:
                    file.write(f"Nome {p} Tarefas: {c} --> {tarefa}\n")
                    c+=1
        case 2:
            print("Quer adicionar tarefa a quem: ")
            with open("ListadeTarefa.txt", "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                   l=linha.split('Tarefas')
                   print(l[0].split('Nome')[1])
                adicionar = input("Sua escolha: ")
                for linha in linhas:
                    if adicionar not in adicionar:
                        print("Pessoa não encontrada.")
                        return 

            while True:
                with open("ListadeTarefa.txt", "r") as file:
                        linhas = file.readlines()
                        for linha in linhas:
                            if adicionar in linha:
                                tarefaantiga=linha.split('-->')
                                tarefas.append(tarefaantiga[1].strip().strip('[]').split(','))
                novaTarefa = input("Tarefa a ser adicionada: ")
                tarefas.append(novaTarefa)
                cont = input("Quer adicionar mais tarefas [s/n]: ").strip().lower()
                
                if cont == 'n':
                    with open("ListadeTarefa.txt", "r") as file:
                        linhas = file.readlines()
                    with open("ListadeTarefa.txt", "w") as file:
                        for linha in linhas:
                            if  adicionar in linha: #Verifica se a pessoa q vou mexer está na inha
                                for i in tarefas:
                                    file.write(f"Nome {adicionar} Tarefas: {len(tarefas)} --> {i}\n")
                            else:
                                file.write(linha)
                    break
        case 3:
            with open("ListadeTarefa.txt", "r") as file:
               linhas = file.readlines()
               for linha in linhas:
                   l=linha.split('Tarefas')
                   print(l[0].split('Nome')[1])
                   
            nome=input("Quer ver tarefa de quem: ")
            with open("ListadeTarefa.txt", "r") as file:
                for linha in linhas:
                    if nome in linha:
                        tarefa = linha.split('-->')[1]
                        tarefa = tarefa.strip().strip("[]").replace("'", "") #strip 1 remove espaços. o 2 os colchetes e o replace troca aspas por nd, só sobrando a virgula
                        mostrar = tarefa.split(',')
                        for t in mostrar:
                            print(f"- {t.strip()}")
        case 4:
            with open("ListadeTarefa.txt", "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    print(linha.split('Tarefas')[0])
                nome=input("Quer remover a tarefa de quem: ")
                for linha in linhas:
                    if nome in linha:
                        tarefa = linha.split('-->')[1]
                        tarefa = tarefa.strip().strip("[]").replace("'", "") #strip 1 remove espaços. o 2 os colchetes e o replace troca aspas por nd, só sobrando a virgula
                        mostrar = tarefa.split(',')
                        for t in mostrar:
                            print(f"- {t.strip()}")
                    excluir=input('Qual tarefa deseja excluir: ')
                    mostrar.remove(excluir)
                    delete=mostrar
                    with open("ListadeTarefa.txt", 'w') as file:
                        file.seek(0)
                        file.readlines()
                        for linha in linhas:
                            if nome in linha:
                                file.write(f"Nome {nome} Tarefas: {len(delete)} --> {delete}\n")
                            else:
                                file.write(linha)

                        

               

                    
                    
       

                
        

               


           
            

