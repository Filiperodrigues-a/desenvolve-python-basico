import random, os, sys

def carregar_palavras():
    with open('gabarito_forca.txt', 'r') as f:
        palavras = f.readlines()
    return [palavra.strip() for palavra in palavras]


def carregar_estagios_enforcado():
    with open('gabarito_enforcado.txt', 'r') as f:
        estagios = f.readlines()
    return [estagio.strip() for estagio in estagios]


def imprime_enforcado(erros, estagios):
    print(estagios[erros])


def jogar_forca():
    
    palavras = carregar_palavras()
    estagios = carregar_estagios_enforcado()
    
   
    palavra = random.choice(palavras)
    palavra_oculta = ['_'] * len(palavra)
    
    tentativas = 6
    erros = 0
    letras_erradas = []
    
    
    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")
    print(" ".join(palavra_oculta))
    
    while erros < tentativas:
        
        tentativa = input("Digite uma letra: ").lower()
        
        
        if tentativa in letras_erradas or tentativa in palavra_oculta:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    palavra_oculta[i] = tentativa
            print("Acertou! Palavra até agora:", " ".join(palavra_oculta))
        else:
            erros += 1
            letras_erradas.append(tentativa)
            print("Errou! Você tem", tentativas - erros, "tentativas restantes.")
            imprime_enforcado(erros, estagios)
        
        
        if '_' not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
    
    if erros == tentativas:
        print("Você perdeu! A palavra era:", palavra)


jogar_forca()