import random

m = random.randint(1, 10)
print(m)
while True:
    n = int(input("Informe um número de 1 a 10: "))
    if m == n:
        print(f"Parabéns você acertou o número escolhido é {n}")
        break
    elif m < n:
        print("Um pouco menos...")
    elif m > n:
        print("Um pouco mais...")
    else:
        print("Valor digitado inválido")

