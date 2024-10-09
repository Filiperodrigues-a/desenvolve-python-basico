n1, n2, n3 = int(input("Informe a 1° nota:")), int(input("Informe a 2° nota:")), int(input("Informe a 3° nota,:")),
m = (n1+n2+n3)/3
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")