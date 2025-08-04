pessoa=dict()
tarefas= list()
def lista(opc):
    
    match opc:
        case 1:
            with open("ListadeTarefa.txt", 'a+') as file:
                file.seek(0)
                linhas=file.readlines()
                nome=input('nome da pessoa: ')
                for linha in linhas:
                    if f"Nome {nome}" in linha:
                        return 'Essa pessoa já foi cadastrada'
                tarefa=input(f"Digite a primeira Tarefa de {nome}: ")
                
                pessoa[nome.strip()]=tarefa
                file.write(f"Nome {nome.strip()} Tarefas: 1 --> {tarefa}\n")
                    
        case 2:
            print("Quer adicionar tarefa a quem: ")
            with open("ListadeTarefa.txt", "r") as f:
                linhas = f.readlines()
                for linha in linhas:
                    print(linha.split('Tarefas')[0].split('Nome')[1].strip())
                
                nome = input("Sua escolha: ").strip()

                for linha in linhas:
                    if f"Nome {nome} " in linha:
                        tarefasAntiga = linha.split('-->')[1].strip()
                        tarefasAntiga= tarefasAntiga.replace('[', '').replace(']', '').replace("'", "")
                        tarefas = []
                        for t in tarefasAntiga.split(','):
                            t_limpa = t.strip()
                            if t_limpa:
                                tarefas.append(t_limpa)

                        pessoa[nome] = tarefas[:]
                        break
                else:
                    return "Pessoa não encontrada."

            while True:
                t = input("Tarefa a ser adicionada: ").strip()
                tarefas.append(t)
                cont = input("Quer adicionar mais tarefas [s/n]: ").strip().lower()
                if cont == 'n':
                    pessoa[nome].extend(tarefas)
                    with open("ListadeTarefa.txt", "w") as f:
                        for linha in linhas:
                            if f"Nome {nome} " in linha:
                                f.write(f"Nome {nome} Tarefas: {len(pessoa[nome])} --> {pessoa[nome]}\n")
                            else:
                                f.write(linha)
                    tarefas.clear()
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
                file.seek(0)
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
                    mostrar.remove(excluir.strip)
                    delete=mostrar
                    with open("ListadeTarefa.txt", 'w') as file:
                        file.seek(0)
                        file.readlines()
                        for linha in linhas:
                            if nome in linha:
                                file.write(f"Nome {nome} Tarefas: {len(delete)} --> {delete}\n")
                            else:
                                file.write(linha)

                        

               

                    
                    
       

                
        

               


           
            

