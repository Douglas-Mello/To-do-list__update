pessoa = dict()
tarefas= list()
def lista(opc):
    match opc:
        case 1:
            with open("ListadeTarefa.txt", 'a+') as file:
                nome=input('nome da pessoa: ')
                c=1
                for k, i in pessoa.items():
                    
                    file.write(f"Nome {k} Tarefas: {c} --> {i} \n")
                    file.write("\n")
                    c+=1
        case 2:
            with open("ListadeTarefa.txt", 'r') as file:

        

               


           
            

