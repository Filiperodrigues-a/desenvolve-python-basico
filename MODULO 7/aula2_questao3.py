import string
def verificar_palindromo(frase):
    frase_nova = ''.join(e.lower() for e in frase if e.isalnum())
    return frase_nova == frase_nova[::-1]
def main():
    while True:
        frase = input("Digite uma frase ou 'fim' para encerrar o programa:")
        if frase.lower() == "fim":
            print("Programa encerrado.")
            break
    if verificar_palindromo(frase):
        print("A frase informada é um palindromo.")
    else:
        print("A frase informada não é um palindromo.")

if __name__ == "__main__":
    main()