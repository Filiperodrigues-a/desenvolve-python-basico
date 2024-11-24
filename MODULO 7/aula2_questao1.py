numero = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12]
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
data = input("Digite a sua data de nascimento na sequência, (dd/mm/aaaa):")
dia, mes, ano = data.split("/")
mes_extenso = meses[int(mes) -1]
print(f"Você nasceu em {dia} de {mes_extenso} do ano de {ano}!")