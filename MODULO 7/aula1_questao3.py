frase = str(input("Digite uma frase: "))
conta_branco = 0
for i in frase:
    if i == ' ':
        conta_branco += 1
        
    
print(conta_branco)