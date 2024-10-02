genero = input("informe seu gênero sexual:")
idade = int(input("Informe sua idade:"))
tempo_servico = int(input("Informe quantos anos trabalhados:"))
a = (genero == 'feminino' and idade >=60) or (genero == 'masculino' and idade >=65)
b = tempo_servico>=30
c = idade>=60 and tempo_servico>=25
pode_aposentar = a or b or c
print(f"Pode aposentar:{pode_aposentar}")