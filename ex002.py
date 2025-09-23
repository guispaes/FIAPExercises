# Uma agência de viagens está propondo uma estratégia para alavancar as vendas após os impactos da pandemia do coronavírus.
# A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma residência.
# Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa.
# Calcule os descontos:
# Econômica:
    # 2 viajantes - 3%
    # 3 viajantes - 4%
    # 4 viajantes ou mais - 5%
# Executiva:
    # 2 viajantes - 5%
    # 3 viajantes - 7%
    # 4 viajantes ou mais - 8%
# Primeira Classe:
    # 2 viajantes - 10%
    # 3 viajantes - 15%
    # 4 viajantes ou mais - 20%

print("<-- DESCONTOS NA VIAGEM -->")

while True:
    categoria_assentos = str(input("As passagens serão Econômicas (EC), Executivas (EX) ou de Primeira Classe (PC)? Utilize o índice: ").upper().replace(" ", ""))
    if categoria_assentos not in ["EC", "EX", "PC"]:
        print("Digite uma categoria válida.")
    else:
        break
quantidade_viajantes = int(input("Quantas pessoas viajarão? "))
valor_bruto = float(input("Qual o valor BRUTO da viagem? R$"))

descontos = {'EC': [0.03, 0.04, 0.05], 'EX': [0.05, 0.07, 0.08], 'PC': [0.10, 0.15, 0.20]}
indice = descontos[categoria_assentos][min(quantidade_viajantes-2, 2)]

if quantidade_viajantes < 2:
    print("Sem descontos dísponiveis.")
else:
    print(f"Desconto aplicado de {str(int(indice*100))}%!"
          f"\nNovo valor: R${valor_bruto - valor_bruto*indice}")
