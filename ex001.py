# Verifique se os batimentos cardíacos por minuto de um usuário encontram na faixa adequada.
# Para isso, você deve solicitar ao usuário que informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE. 
# A partir disso, o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada
# Até 3 anos: 98 a 140 BPM
# De 3 a 5 anos: 80 a 120 BPM
# De 6 anos até 12 anos: 75 a 118 BPM
# A partir de 13 anos: 60 a 100
# A partir de 60 anos: 50 a 60 BPM

print('<-- MONITORAMENTO DE BPM -->')
idade = int(input('Qual a idade do paciente? '))
velocidade_bpm =  int(input('Qual é a frequência cardíaca do paciente? '))

if idade <= 2:
    menor_frequencia, maior_frequencia = 98, 140
elif idade >=3 and idade<=5:
    menor_frequencia, maior_frequencia = 80, 120
elif idade >= 6 and idade <= 12:
    menor_frequencia, maior_frequencia = 75, 118
elif idade >= 13 and idade <=60:
    menor_frequencia, maior_frequencia =  60, 100
else:
    menor_frequencia, maior_frequencia = 50,  60

if velocidade_bpm >= menor_frequencia and  velocidade_bpm <= maior_frequencia:
    print('O BPM do paciente está regulada.')
else:
    print('O BPM do paciente está desregulada.')
