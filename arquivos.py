def arquivo(opc):
    tarefa=[]
    pessoa={}
    if opc in  range(3,6):
        with open("ListadeTarefas.txt", "a+") as file:
            if opc == 3:
               print()    
            elif opc ==4:
                file.seek(0)
                msg=file.read()
                if msg.strip() == "":
                    print("Sem tarefas no momento")
                else:
                    print(f"\033[32m{msg}\033[0m")
            elif opc == 5:
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
    else:
        if opc == 1:
            nome=input("Digite o nome da Pessoa: ")
            tarefa.append(input(f"Qual tarefa deseja atirbuir à {nome}: "))
            pessoa[nome]=tarefa[:]
        elif opc == 2:
            print("Deseja adicionar Tarefa para quem")
            for k in pessoa.keys():
                print(k)
            
                
               


           
            

