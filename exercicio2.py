# Variáveis
valor_base_mensalidade = float(input("Valor da mensalidade: ")) #Recebe o valor da mensalidade
nota = float(input("Nota média: ")) #Recebe a nota
dia_pagamento = int(input("Dia do pagamento: "))  #Recebe o dia do pagamento
monitor = str(input("É monitor? (s/n): ")) #Verifica se é monitor

#Dia do pagamento
valor = valor_base_mensalidade #Guarda o valor inicial
if dia_pagamento <= 5: #Verifica se pagou até o dia 5
  valor = valor - 100 #Aplica desconto de R$ 100
else:
    if dia_pagamento >=15:  #Verifica se pagou após o dia 15
      valor = valor + 50  #Aplica multa de R$ 50


#Bolsa
if nota >= 9:   #Verifica se a nota é pelo menos 9
    valor = valor*0.8   #Aplica desconto de 20%
else:
    if nota >= 7:  # Verifica se a nota está entre 7 e 9
        valor = valor*0.9  #Aplica desconto de 10%
    else:
        print("Atenção: Procure a coordenação para apoio pedagógico.")  #Exibe aviso para nota abaixo de 7

#Monitoria
if monitor == "s":  #Verifica se o aluno é monitor
    valor = valor - 50  #Aplica desconto de R$ 50

#Resultado final

print(f"Mensalidade final: R$ {valor:.2f}")  #Exibe o valor final