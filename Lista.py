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
        opc('Adicionar tarefa', 1)
        opc('Listar tarefas', 2)
        opc ('Remover tarefa', 3)
        opc ('Sair', 4)
        resp = int(input("Opção: "))
        sleep(1)
        if resp in range(1,4):
            arquivo(resp)
            sleep(2)
        elif resp == 4:
            Print('Saindo...')
            sleep(1.3)
        else:
            print("Opção inválida")
            sleep(2)
    except ValueError:
        print('Digite apenas números inteiros e dentro das opções disponivéis')
        sleep(2)
