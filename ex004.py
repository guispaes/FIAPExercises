# Um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. 
# O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.
# A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura: 
# Basic     : 30%
# Silver    : 20%
# Gold      : 10%
# Platinum  : 05%

taxa = {'Basic': 0.30, 'Silver': 0.20, 'Gold': 0.10, 'Platinum': 0.05}

print(f'Tipos de assinatura:\n-Basic\n-Silver\n-Gold\n-Platinum\n')

while True:
    assinatura = str(input(f'Qual o tipo de assinatura do cliente? ').replace(" ", "").capitalize())
    if assinatura not in taxa.keys():
        print(f"\nPor favor, digite um tipo de assinatura válido.")
    else:
        break
faturamento_anual = float(input("Qual o faturamento anual do cliente? R$"))

print(f"A taxa aplicada para o tipo de assinatura {assinatura} é de {int(taxa[assinatura]*100)}%\n"
      f"Faturamento anual: R${faturamento_anual:.2f}\n"
      f"Valor a ser pago pelo cliente: R${faturamento_anual*taxa[assinatura]:.2f}")
