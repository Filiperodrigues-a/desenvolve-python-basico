import random
def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []
    

    for palavra in palavras:
        if len(palavra) > 3:
            inicio = palavra[0]
            fim = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = inicio + ' '.join(meio) + fim
        else:
            nova_palavra = palavra
        nova_frase.append(nova_palavra)
    return ' '.join(nova_frase)
frase = input("Digite uma frase que será codificada:")
resultado = embaralhar_palavras(frase)
print(resultado)