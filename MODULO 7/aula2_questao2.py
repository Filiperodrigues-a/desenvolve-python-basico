frase = input("Escreva uma frase: ")
frase.lower()
nova_frase = frase.replace("a", "*")
nova_frase1 = nova_frase.replace("e", "*")
nova_frase2 = nova_frase1.replace("i", "*")
nova_frase3 = nova_frase2.replace("o", "*")
nova_frase4 = nova_frase3.replace("u", "*")
print(f"A nova frase ficou: {nova_frase4.capitalize()}")