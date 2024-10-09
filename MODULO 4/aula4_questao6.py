n = int(input("informe a quantidade de experimentos realizados:"))
#inicializar as variaveis
cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0
while cont < n:
    cont += 1
    quantidade = int(input("Informe a quantidade de cobaias:"))
    tipo = input("Informe o tipo de Cobaia: Rato(R), Sapo(S), Coelho(C)")
    if tipo == 'S':
        soma_sapo += quantidade
    elif tipo == 'R':
        soma_rato += quantidade
    elif tipo == 'C':
        soma_coelho += quantidade
    else: print("Cobaia invalida.")

total_cobaias = soma_coelho+soma_rato+soma_sapo
print(f"Total de cobais:{total_cobaias}")
print(f"Total de sapos:{soma_sapo}")
print(f"Total de coelhos:{soma_coelho}")
print(f"Total de ratos:{soma_rato}")
print(f"Percentual de sapos:{(soma_sapo/total_cobaias)*100}%")
print(f"Percentual de coelhos:{(soma_coelho/total_cobaias)*100}%")
print(f"Percentual de ratos:{(soma_rato/total_cobaias)*100}%")