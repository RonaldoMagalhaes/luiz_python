"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:


    print("Selecione uma opção: ")
    op = input("[i]nserir [a]pagar [l]istar: ")
    match op:

        case"l":
            if len(lista) == 0:
                os.system('clear')
                print("Nada para listar")
            else:
                os.system('clear')
                for i,v in enumerate(lista):
                    print(i, v)
        case "a":
            if len(lista) == 0:
                print("Nada para apagar")
                continue
            ind = input("Escolha o índice para apagar: ")
            try:
                indice = int(ind)
                if indice > 1:
                    os.system('clear')
                    print("Indice incorreto, tente novamente")
                    continue
                if indice > len(lista):
                    os.system('clear')
                    print("Não foi possível apagar este índice")
                    continue
                else:
                    os.system('clear')
                    del lista[indice]
                    print("O item foi removido de sua lista")
            except:
                os.system('clear')
                print("Indice incorreto, tente novamente")
                continue

        case "i":
            os.system('clear')
            val = input("Valor: ")
            lista.append(val)
            print("Item adicionado com sucesso...")

        case _:
            print("Opcao Invalida")


