import os
lista = []
opcao = -1

def inserir(n):
    lista.append(n)

def remover(n):
    while n in lista:
        lista.remove(n)

def listar():
    print(lista)

while (opcao!=0):
    print("\n|=========================|")
    print("|       .::MENU::.        |")
    print("| 1 - Inserir elemento    |")
    print("| 2 - Retirar elemento    |")
    print("| 3 - Printar lista       |")
    print("| 0 - Sair do Programa    |")
    print("|      ..::====::..       |")
    print("|=========================|")
    opcao = int(input("Digite a opção desejada: "))
    os.system('cls')

    if(opcao==0):
        print("Até mais!")
    elif (opcao==1):
        inserir(input("Digite o valor para ser inserido: "))
    elif (opcao==2):
        remover(input("Digite o valor para ser removido: "))
    elif (opcao==3):
        print("..::Printando a lista::..")
        listar()
    else:
        print("Opção inválida!")