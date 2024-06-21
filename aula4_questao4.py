n = int(input("Informe um número:"))
maior = 0
while n > 0:
    x = int(input("Informe o valor de 'x'"))
    if x > maior:
        maior = x
        n = n -1
    elif x < maior:
        n = n -1
print(maior)