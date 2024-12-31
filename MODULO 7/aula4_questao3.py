import os, sys, re
caminho_arquivo = 'estomago.txt'
def contar_mencao(nome, texto):
    return len(re.findall(r'\b' + re.escape(nome) + r'\b', texto, re.IGNORECASE))

with open(caminho_arquivo, 'r',) as arquivo:
    linhas = arquivo.readlines()
    print("Primeiras 25 linhas:")
    for i in range(min(25, len(linhas))):
        print(linhas[i], end='')
    print("\n")

    num_linhas = len(linhas)

    linha_com_mais_caracteres = max(linhas, key=len)
    print(f"Linha com maior número de caracteres:\n{linha_com_mais_caracteres}")

    mencao_nonato = contar_mencao("Nonato", ''.join(linhas))
    mencao_iria = contar_mencao("Íria", ''.join(linhas))
    print(f"Menções a 'Nonato': {mencao_nonato}")
    print(f"Menções a 'Íria': {mencao_iria}")
