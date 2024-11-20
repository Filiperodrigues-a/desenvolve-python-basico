frase = str(input("Digite uma frase:"))
count_vogais = 0
indices = []
for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        count_vogais += 1
        indices.append(i)
print(f"Número de vogais: {count_vogais}")
print(indices)