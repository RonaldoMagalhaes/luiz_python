frase = 'O Python é uma linguagem de programacao'\
    'multiparadigma.' \
    'Python foi criado por Guido Van Russon.'


print(frase.count("Python"))

ind = 0

while ind < len(frase):
    letra = frase[ind]
    qts_vezes = frase.count(letra)

    print("=" * 55)
    print(f"{letra} apareceu {qts_vezes} vezes")

    ind += 1
