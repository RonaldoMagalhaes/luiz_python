"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))


l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2

print()
print(l3) # [1, 2, 3, 4, 5, 6]

print()
print(l1)
l1.extend(l2)
print(l1) # [1, 2, 3, 4, 5, 6]




