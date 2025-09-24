# Os colaboradores da sua equipe foram sorteados para ganhar um console de última geração, cada um, em razão do bom desempenho que tiveram nos últimos projetos. 
# Por uma questão de logística, porém, a empresa pede que todos os cinco membros da equipe recebam o mesmo aparelho.
#Crie um algoritmo em que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos. 
# As opções são: PLAYSTATION, XBOX e NINTENDO. 

votacao = {'Playstation': 0, 'Xbox': 0, 'Nintendo': 0}

print(f"Qual console deve ser entregue aos colaboradores?\n\nOpções:\n\nPlaystation\nXbox\nNintendo\n")

for c in range(1,6):
    while True: 
        voto = input(f"Voto {c}: ").capitalize().replace(' ','')
        if voto not in votacao.keys():
            print("Por favor, digite uma opção válida.")
        else:
            break
    votacao[voto] += 1

ranking = sorted(votacao.items(), key= lambda valor: valor[1],reverse=True)
print(f"\n<-- Ranking final -->\n")                  
for c, (console, votos) in enumerate(ranking):
    print(f'{c+1}- {console} - Votos: {votos}')

print(f"\nO console a ser entregue aos colaboradores será o {ranking[0][0]}!")
