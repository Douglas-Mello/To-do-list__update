pessoa = dict()

def lista(opc):
    tarefas= list()
    match opc:
        case 1:
            with open("ListadeTarefa.txt", 'a+') as file:
                nome=input('nome da pessoa: ')
                c=1
                tarefa=input(f"Digite a primeira Tarefa de {nome}: ")
                pessoa[nome]=[tarefa]
                for k, i in pessoa.items():
                    
                    file.write(f"Nome {k} Tarefas: {c} --> {i}\n")
                    c+=1
        case 2:
            print("Quer adicionar tarefa a quem: ")
            for k in pessoa.keys():
                print(f"- {k}")
            adicionar = input("Sua escolha: ")
            if adicionar not in pessoa:
                print("Pessoa não encontrada.")
                return 

            while True:
                novaTarefa = input("Tarefa a ser adicionada: ")
                tarefas.append(novaTarefa)
                cont = input("Quer adicionar mais tarefas [s/n]: ").strip().lower()
                
                if cont == 'n':
                    pessoa[adicionar] += tarefas
                    with open("ListadeTarefa.txt", "r") as file:
                        linhas = file.readlines()
                    with open("ListadeTarefa.txt", "w") as file:
                        for linha in linhas:
                            if  adicionar in linha: #Verifica se a pessoa q vou mexer está nal inha
                                file.write(f"Nome {adicionar} Tarefas: {len(pessoa[adicionar])} --> {pessoa[adicionar]}\n")
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
                   l=linha.split('Tarefas')
                   print(l[0].split('Nome')[1])
                   
            nome=input("Quer excluir a tarefa de quem: ")
            with open("ListadeTarefa.txt", "r") as file:
                for linha in linhas:
                    if nome in linha:
                        tarefa = linha.split('-->')[1]
                        tarefa = tarefa.strip().strip("[]").replace("'", "") 
                        mostrar = tarefa.split(',')
                        for t in mostrar:
                            print(f"- {t.strip()}")
                        excluir=input("Qual tarefa deseja excluir: ")
                        if excluir in mostrar:
                            tarefas=mostrar
                            tarefas.remove(excluir)
            with open("ListadeTarefas.txt", "a+") as file:
                file.seek(0)
                for linha in linhas:
                    if nome in linha:
                        file.write()
                
               

                    
                    
       

                
        

               


           
            

