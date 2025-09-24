# Elabore um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu em uma refeição.
# Após isso o usuário deve informar o número de calorias de cada um dos alimentos.
# No final, o programa deve exibir o total de calorias da refeição.

refeicao = {}

for c in range(0, int(input("Quantos alimentos diferentes tem no prato? "))):
    alimento = str(input(f"Qual é o {c+1}° alimento? ").capitalize().strip())
    calorias = float(input(f"Quantas calorias de {alimento}? "))
    refeicao[alimento] = calorias

print(f"Alimentos: {"; ".join(list(refeicao.keys()))}\n"
      f"Quantidade total de calorias: {sum(refeicao.values()):.1f}")
