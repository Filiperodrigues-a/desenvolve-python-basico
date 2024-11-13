    import random

lista1, lista2 = [], []
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))
interseccao = []
for elemento in lista1:
    if elemento in lista2:
        interseccao.append(elemento)
interseccao.sort()
for i in interseccao:
    print(f"{i}: ({(lista1.count(i))}, {lista2.count(i)})")

print("Lista 1:", lista1)
print("Lista 2:",lista2)
print("Lista de interseccao: ", interseccao)