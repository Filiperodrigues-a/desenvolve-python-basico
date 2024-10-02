comprimento = int(input("Informe o comprimento do terreno:"))
largura = int(input("Informe a largura do terreno:"))
preco_m2 = float(input("Informe o valor do metro quadrado:"))
#calculo da área do terreno
area = comprimento*largura
#calculo do valor do metro quadrado do terreno
valor_terreno = area*preco_m2
#resultado da operação informando a área do terreno e seu respectivo valor.
print(f"O terreno possui {area}m2 e custa R${valor_terreno:,.2f}.")