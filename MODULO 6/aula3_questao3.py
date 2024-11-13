import random
lista = []
for i in range(20):
    lista.append(random.randint(-10, 10))
print("Lista antes da deleção: ",lista)

indice_fatia_maior, tamanho_fatia_maior = 0, 0 
indice_fatia_atual, tamanho_fatia_atual = 0, 0
for i in range(len(lista)):
    if lista [i] < 0:
        tamanho_fatia_atual += 1
        if tamanho_fatia_atual == 1:
            indice_fatia_atual = i
    else:
        if tamanho_fatia_atual > tamanho_fatia_maior:
            tamanho_fatia_maior = tamanho_fatia_atual
            indice_fatia_maior = indice_fatia_atual 
        tamanho_fatia_atual = 0 
del lista[indice_fatia_maior:indice_fatia_maior+tamanho_fatia_maior]

print("A lista após deletar a maior fatia negativa ficou: ",lista)
