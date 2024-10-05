classe = input("Escolha uma classe para seu personagem: Guerreiro, Mago ou Arqueiro:")
forca = int(input("Digite os pontos de força (de 1 a 20):"))
magia = int(input("Digite os pontos de magia (de 1 a 20):"))
guerreiro = forca>=15 and magia<=10
mago = forca <=10 and magia>=15
arqueiro = (forca>5 and forca<=15) and (magia>5 and magia<=15)
if classe == "guerreiro":
    print(f"Pontos de atributo consistentes com a classe escolhida: {guerreiro}")
elif classe == "mago":
    print(f"Pontos de atributo consistentes com a classe escolhida: {mago}")
elif classe == "arqueiro":
    print(f"Pontos de atributo consistentes com a classe escolhida: {arqueiro}")
else:
    print(f"Classe invalida.")
