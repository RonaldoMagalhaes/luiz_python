"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite o seu primeiro nome: ")

try:
    if nome.isalpha():
        l = len(nome)
        if l <=4:
            print("Seu nome é curto")
        elif l <= 6:
            print("Seu nome é normal")
        else:
            print("Seu nome é muito grande")
    else:
        print("Erro => Valor incorreto para nome")

except:
    print("Erro => Valor incorreto para nome")
