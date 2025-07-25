def arquivo(opc):
    
    with open("ListadeTarefas.txt", "a+") as file:
        if opc == 1:
            file.seek(0)
            qtdL = file.readlines()
            tarefa = input("\nQual tarefa deseja adicionar: ")
            file.write(f"{len(qtdL) +1} ==> {tarefa} \n")
            print("Tarefa adicionada com sucesso")        
        elif opc ==2:
            file.seek(0)
            msg=file.read()
            if msg.strip() == "":
                print("Sem tarefas no momento")
            else:
                print(f"\033[32m{msg}\033[0m")
        else:
            file.seek(0)
            msg=file.read()
            if msg.strip() == "":
                print("Sem tarefas no momento")
            else:
                try:
                    with open("ListadeTarefas.txt", "r") as file:
                        lista=file.readlines()
                    print("Qual tarefa deseja excluir")
                    for i,t in enumerate(lista):
                        print(f"{t}",end="\n")
                    remover=int(input('Tarefa a ser removida: ')) - 1
                    del lista[remover]
                    with open("ListadeTarefas.txt", "w") as file:
                        for i,l in enumerate(lista):
                            conteudo =l.split('==>', 1)[-1].strip()
                            file.write(f"{i+1} ==> {conteudo}\n")
                    print("Tarefa removida com sucesso")
                except:
                    print(NameError)
                
               


           
            

