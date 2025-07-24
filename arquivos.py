def arquivo(opc):
    with open("ListadeTarefas.txt", "a+") as file:
        if opc == 1:
            file.seek(0)
            qtdL = file.readlines()
            tarefa = input("Qual tarefa deseja adicionar: ")
            file.write(f"{len(qtdL) +1} ==> {tarefa}")
        elif opc ==2:
            file.seek(0)
            msg=file.read()
            print(msg)
        else:
            file.seek(0)
            lista=file.readlines()
            print("Qual tarefa deseja excluir")
            for i,t in enumerate(lista):
                print(f"{t}")
            remover=int(input('Tarefa a ser removida: ')) - 1
            del lista[remover]
            with open("ListadeTarefas.txt", "w") as file:
                for i,l in enumerate(lista):
                    file.write(f"{i+1} ==> {l}")


           
            

