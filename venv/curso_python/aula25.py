"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))


n = 15
print()
print("O hexadecimal de %d é %X" % (n,n))
# O hexadecimal de 15 é F


n = 15
print()
print("O hexadecimal de %d é %04X" % (n,n))
# O hexadecimal de 15 é 000F

