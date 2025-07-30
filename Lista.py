from arquivos import *
from time import sleep
def Print(txt):
    print("-"* (len(txt) + 4))
    print(txt.center((len(txt) + 4)))
    print("-"* (len(txt) + 4))
def opc(txt, c):
    print(f"opção {c} --> {txt} ")
    

Print("Selecione a opção desejada ")
while True:
    try:
        opc('Adicionar pessoa',1)
        opc("Adicionar tarefa",2)
        opc('Listar tarefas', 3)
        opc ('Remover tarefa', 4) 
        opc ('Sair', 5)
        resp = int(input("Opção: "))
        
        if resp in range(1,5):
            print()
            lista(resp)
            sleep(1.5)
        elif resp == 5:
            Print('Saindo ...')
            sleep(1.5)
            break
            
        else:
            print("\033[31mOpção inválida\033[0m")
           
    except ValueError:
        print( "\033[31mDigite apenas números inteiros e dentro das opções disponivéis\033[0m")
        sleep(2)
