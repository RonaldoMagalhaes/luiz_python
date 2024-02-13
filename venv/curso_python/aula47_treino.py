"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = "pearl"
tentativas = []

tamanho = len(palavra_secreta)

rascunho = []

for _ in palavra_secreta:
    rascunho.append("*")

while "*" in rascunho:

    print("Tente adivinhar a palavra secreta:")
    print(rascunho)

    tentativas_user = input("Escolha uma letra: ")
    tentativas.append(tentativas_user)

    if tentativas_user in palavra_secreta:
        res = palavra_secreta.index(tentativas_user)
        rascunho[res] = tentativas_user

    print(rascunho)
    print(tentativas)

    input("Tecle enter para continuar")
    os.system('clear')

