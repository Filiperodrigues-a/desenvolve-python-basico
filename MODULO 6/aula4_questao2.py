frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

lista_vogais = sorted([letra for letra in frase if letra in vogais])
lista_consoantes = sorted([letra for letra in frase if letra.isalpha() and letra not in vogais])


print(f"Lista de vogais ordenadas: {lista_vogais}")
print(f"Lista de consoantes ordenadas: {lista_consoantes}")