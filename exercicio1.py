#auditoria automatizada de turmas #
quantidade_alunos = int(input("Digite a quantidade de alunos: "))


while quantidade_alunos <= 0:
    print("A quantidade de alunos deve ser maior que zero.")
    quantidade_alunos = int(input("Digite a quantidade de alunos: "))

aprovados = 0
reprovados = 0
exame_final = 0

print("\n" + "-" * 50)
print("INICIANDO PROCESSAMENTO DA TURMA")
print("-" * 50)

total_faltas = 0
soma_notas = 0

for aluno in range(1, quantidade_alunos + 1):
    nome = input("Nome do aluno(a): ")
    
    total_faltas = 0
    soma_notas = 0

    for avaliacao in range(1, 4):
        nota = float((input(f"Digite a nota da {avaliacao}º avaliação: " )))
        while nota < 0 or nota > 10:
            print( "Nota inválida, digite novamente.")
            nota = float(input(f"Digite a nota da {avaliacao}º avaliação: "))
        soma_notas += nota
    for frequencia in range(1, 5):
        falta = int(input(f"Digite a quantidade de faltas na {frequencia}º etapa: "))
        while falta < 0:
            print("Valor inválido, digite novamente!")
            falta = int(input(f"Digite a quantidade de faltas na {frequencia}º etapa: "))
        total_faltas += falta


    nota_final = soma_notas/3

    if total_faltas > 15:
        situacao = "REPROVADO POR FALTA"
        reprovados += 1
    elif nota_final >= 7:
        situacao = "APROVADO"
        aprovados += 1
    elif total_faltas <= 15 and nota_final >=4:
        situacao = "EXAME FINAL"
        exame_final += 1
    else:
        situacao = "REPROVADO POR NOTA"
        reprovados += 1

    print("\n" + "-" * 40)
    print(f"BOLETIM AUDITADO - {nome}")
    print(f"Média Final: {nota_final:.2f}")
    print(f"Total de Faltas: {total_faltas}")
    print(f"Situação Final: {situacao}")
    print("-" * 40)

print("\n" + "-"*50)
print("=== FINALIZAÇÃO E IMPRESSÃO DOS DIÁRIOS DA CLASSE ===")
print( "-"*50)

for numero in range(1, quantidade_alunos + 1):
    print(f" -> Gerando e autenticando via sistema a acta digital Nº {numero:03d}/{quantidade_alunos:03d}...")

print("=== RESUMO GERAL DA TURMA ===")
print(f"Total de alunos auditados: {quantidade_alunos} ")
print(f"Alunos reprovados: {reprovados}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em exame final (NOTA/FALTA): {exame_final}")
print("-"*50)
