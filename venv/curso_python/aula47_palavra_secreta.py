
palavra_secreta = "nirvana"
tentativas = 0
letras_acertadas = ""

while True:
    letra_digitada = input("Digite uma letra: ")
    if len(letra_digitada) > 1:
        print("Digite apenas 1 letra.")
        continue
    tentativas += 1
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    if palavra_formada == palavra_secreta:
        print(f"Parabéns. A palavra secreta é {palavra_secreta}")
        print(f"Tentativas: {tentativas}")
        break

    else:
        print(palavra_formada)
