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
        opc('Salvar tarefa', 3)
        opc('Listar tarefas', 4)
        opc ('Remover tarefa', 5)
        opc ('Sair', 6)
        resp = int(input("Opção: "))
        
        if resp in range(1,6):
            print()
            arquivo(resp)
            sleep(1.5)
        elif resp == 6:
            Print('Saindo ...')
            sleep(1.5)
            break
            
        else:
            print("\033[31mOpção inválida\033[0m")
           
    except ValueError:
        print( "\033[31mDigite apenas números inteiros e dentro das opções disponivéis\033[0m")
        sleep(2)
