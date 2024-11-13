import random
for i in range(1):
    num_elementos = random.randint(5, 20)
    print(num_elementos)
elementos = []
for i in range(num_elementos):
    x = random.randint(1, 10)
    elementos.append(x)

#imprima a lista elementos
print("lista:", elementos)
# a soma dos valores da lista
print("a soma dos valores da lista", sum(elementos))
#o indice do menor valor da lista
print("indice do menor valor da lista", elementos.index(min(elementos)))