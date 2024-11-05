from datetime import datetime

data_atual = datetime.now()
data_formatada = data_atual.strftime('%d/%m/%Y')
hora_formatada = data_atual.strftime('%H:%M:%S')
print(f"Data {data_formatada} e hora {hora_formatada}")