filme = str(input("Informe o nome do filme que deseja fazer uma avaliação:"))
nota = int(input(f"Dê sua avaliação sobre o filme {filme} de 1 a 5, onde 1 é Ruim e 5 Excelente: "))
if nota == 5:
    print(f"O filme {filme} é Excelente")
elif nota == 4:
    print(f"O filme {filme} é Muito Bom")
elif nota == 3:
    print(f"O filme {filme} é Bom")
elif nota == 2:
    print(f"O filme {filme} é Regular")
else:
    print(f"O filme {filme} é Ruim")
