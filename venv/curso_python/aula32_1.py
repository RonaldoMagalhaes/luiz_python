"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_str = input("Entre com um número inteiro: ")

try:
    num = int(num_str)

    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")

except:
    print("Valor digitado nao eh um número inteiro")


