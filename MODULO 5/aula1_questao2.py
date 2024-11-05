import random, math

n = int(input("Selecione a quantidade de números que deseja selecionar aleatóriamente: "))
soma = 0
print(n)
for i in range(n):
    soma += random.randint(0, 100)
print(soma)
print(f"a raiz da soma dos {n} número(s) escolhidos é {math.sqrt(soma):.3f}")