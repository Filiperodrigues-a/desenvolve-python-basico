#lista 1
lista1 = [20]
for i in range(20, 50, 2):

    lista1.append(i+2)
print("Todos os números pares entre 20 e 50 da lista 1:",lista1)

#lista 2
lista2 = [x**2 for x in range(1, 10)]

print("lista2",lista2)

#lista 3
lista3 = []
for i in range(1, 101):
    if (i) % 7 == 0:
        lista3.append(i)
    


print("lista 3:",lista3)

#lista 4
lista4 = []
for i in range(0, 30, 3):
    if i % 2 == 0:
        print(f"{i} Par")
        lista4.append(i)
    else:
        print(f"{i} impar")
        lista4.append(i)
print(f"lista4 {lista4}")