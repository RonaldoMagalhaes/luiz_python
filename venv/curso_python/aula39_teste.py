nome = "Luiz Otavio"

indice = 0
str1 =""
str2=""

while indice < len(nome):
    letra = nome[indice]
    str1 += letra
    str2 += letra+"*"
    indice += 1

print(str1)
print(str2)
