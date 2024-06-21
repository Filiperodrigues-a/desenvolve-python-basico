#Quantidade de entrevistados
n = int(input("Quantas pessoas foram entrevistadas:"))
#inicializar variaveis
soma = 0
cont = 0
while cont < n:
    idade = int(input())
    soma += idade
    cont += 1

resultado = (soma/n)
print(f"A média de idade dos entrevistados é:{resultado:.0f} anos")