distancia = int(input("Informe a distância da entrega em Km:"))
peso = float(input("Informe o peso em Kg:"))

# tarifa por distancia
if distancia <= 100:
    tarifa = 1
elif 101 <= distancia <=300:
    tarifa = 1.5
else:
    tarifa = 2

#calculando o frete
frete = tarifa * peso

#verificar taxa de sobrepeso
if peso >10:
    frete += 10


print(f"O valor do frete é R${frete}")