numero = int(input("informe seu número: "))

if numero // 100000000 == 0:
    numero = 900000000 + numero
    n1 = numero // 10000
    n2 = numero % 10000
    print(f"Número completo {n1}-{n2}")
elif numero // 1000000000 == 0:
    n1 = numero // 10000
    n2 = numero % 10000
    print(f"Número completo {n1}-{n2}")
else:
    print("Número incorreto")
