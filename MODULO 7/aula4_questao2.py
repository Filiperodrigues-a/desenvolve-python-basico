import re, os

caminho_arquivo_frase = os.path.join(os.getcwd(), "frase.txt")

with open(caminho_arquivo_frase, "r") as arquivo:
    frase = arquivo.read()
palavras = re.findall(r'[a-zA-Z]+', frase)
caminho_arquivo_palavras = os.path.join(os.getcwd(), "palavras.txt")
with open(caminho_arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")
with open(caminho_arquivo_palavras, "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo 'palavras.txt':")
    print(conteudo)