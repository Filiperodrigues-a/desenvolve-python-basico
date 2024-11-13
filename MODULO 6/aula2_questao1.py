import random
valor = []
for i in range(20):
    x = random.randint(-100, 100)
    valor.append(x)
#lista ordenada
print(sorted(valor))
#lista original
print(valor)
# indice do maior valor da lista
print("O maior valor está no index: ", valor.index(max(valor)))
# indice do menor valor da lista
print("O menor   valor está no index: ", valor.index(min(valor)))