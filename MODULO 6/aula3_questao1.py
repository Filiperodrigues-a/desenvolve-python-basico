lista = [] 
cont = 0
while True:
    valor = int(input("Informe uma quantidade indefinida de números inteiros, digite 00 para finalizar: "))
    if valor == 00:
        break
    lista.append(valor)
    cont += 1
    if cont < 4:
        print("Informe no mínimo 4 números.")

    
# lista original    
print("A lista criada é: ",lista)

print("Os 3 primeiros elementos são:",lista[:3:])

print("Os 2 últimos elementos são:",lista[-1:-3:-1])

print("A lista invertida:",lista[::-1])

print("elementos de indice par:",lista[0::2])

print("elementos de indice impar:",lista[1::2])