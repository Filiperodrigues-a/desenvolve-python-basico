t_fahrenheit = int(input("Informe a temperatura em Fahrenheit:"))
#formula de conversão Fahrenheit para Celsius 
t_celsius = (t_fahrenheit-32)*(5/9)
#conversão de número flutuante para número inteiro
t_celsius = int(t_celsius)
print(f"{t_fahrenheit} graus Fahrenheit são {t_celsius} graus Celsius.")