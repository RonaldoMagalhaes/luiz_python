# Calculadora com while
import os

loop = "s"

while loop != "n":

    n1_str = input("Digite um numero: ")
    n2_str = input("Digite outro numero: ")

    try:
        n1 = float(n1_str)
        n2 = float(n2_str)


        operador = input("Digite um operador <+ - / *>: ")

        match operador:
            case "+":
                print(f"{n1} + {n2} = {n1+n2}")

            case "-":
                print(f"{n1} - {n2} = {n1-n2}")

            case "/":
                print(f"{n1} / {n2} = {n1/n2}")

            case "*":
                print(f"{n1} * {n2} = {n1*n2}")

            case _:
                print(f"Operador inválido. Tente novamente...")

        loop = input("Deseja continuar? <s/N>: ").lower()
        os.system('clear')

    except:
        print("Erro => Os Valores precisam ser números")


