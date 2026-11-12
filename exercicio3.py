# =====================================================================
# SISTEMA DE GESTÃO DE FINANÇAS E RU DA VIDA ESTUDANTIL
# =====================================================================
 
# ---------------------------------------------------------------------
# 1. INICIALIZAÇÃO: dados básicos do estudante
# ---------------------------------------------------------------------
saldo = float(input("Informe o saldo inicial da conta: R$ "))
categoria = input("Informe a categoria (A = Bolsista / R = Regular): ")
 
# Repete ENQUANTO a categoria for inválida (validação de entrada com while)
while categoria != "A" and categoria != "R":
    print("Categoria inválida! Digite A ou R.")
    categoria = input("Informe a categoria (A = Bolsista / R = Regular): ")
 
VALOR_TICKET = 2.50  # valor padrão do ticket do RU
 
# Variáveis contadoras e acumuladoras (começam em zero)
total_tickets = 0         # contadora: tickets do RU comprados
total_alimentacao = 0.0   # acumuladora: gasto com alimentação
total_despesas = 0.0      # acumuladora: gasto com despesas gerais
 
opcao = 0  # valor inicial para entrar no laço do menu
 
# ---------------------------------------------------------------------
# 2. MENU PRINCIPAL: fica ativo ENQUANTO o usuário não escolher 4
# ---------------------------------------------------------------------
while opcao != 4:
    print("\n=== SISTEMA DE GESTÃO FINANCEIRA ESTUDANTIL ===")
    print("1 - Comprar Tickets do RU")
    print("2 - Processar Lote de Despesas Diárias")
    print("3 - Consultar Extrato Consolidado")
    print("4 - Sair do Sistema")
    opcao = int(input("Escolha uma opção: "))
 
    # -----------------------------------------------------------------
    # 3. OPÇÃO 1: COMPRAR TICKETS DO RU
    # -----------------------------------------------------------------
    if opcao == 1:
        quantidade = int(input("Quantos tickets deseja comprar? "))
 
        # Define o valor unitário do ticket
        if categoria == "A" or (saldo < 20 and quantidade <= 5):
            valor_unitario = 0.0            # isento / subsidiado
        elif categoria == "R" and quantidade >= 10:
            valor_unitario = 1.50           # desconto por lote
        else:
            valor_unitario = VALOR_TICKET   # valor integral
 
        custo_total = quantidade * valor_unitario
 
        # Validação de saldo
        if custo_total <= saldo:
            saldo = saldo - custo_total
            total_tickets += quantidade
            total_alimentacao += custo_total
            print("Compra aprovada!")
        else:
            print("Saldo insuficiente para realizar esta compra!")
 
    # -----------------------------------------------------------------
    # 4. OPÇÃO 2: PROCESSAR LOTE DE DESPESAS DIÁRIAS
    # -----------------------------------------------------------------
    elif opcao == 2:
        qtd_despesas = int(input("Quantas despesas deseja cadastrar hoje? "))
 
        # Número de repetições conhecido -> laço for
        for i in range(1, qtd_despesas + 1):
            descricao = input(f"Descrição da {i}ª despesa: ")
            valor = float(input(f"Valor da {i}ª despesa: R$ "))
 
            if valor > saldo:
                print(f"Despesa '{descricao}' recusada: ultrapassa o saldo atual.")
            else:
                saldo = saldo - valor
                total_despesas += valor
                print(f"Despesa '{descricao}' registrada!")
 
    # -----------------------------------------------------------------
    # 5. OPÇÃO 3: EXTRATO CONSOLIDADO
    # -----------------------------------------------------------------
    elif opcao == 3:
        total_gastos = total_alimentacao + total_despesas
 
        print("\n--- EXTRATO CONSOLIDADO ---")
        print(f"Saldo Atual Restante: R$ {saldo:.2f}")
        print(f"Quantidade Total de Tickets do RU adquiridos: {total_tickets}")
        print(f"Total Geral Acumulado de Gastos no Mês: R$ {total_gastos:.2f}")
 
        if saldo < 10 and total_gastos > 100:
            print("ALERTA VERMELHO: Orçamento crítico! Reduza os gastos imediatamente.")
 
    # -----------------------------------------------------------------
    # 6. OPÇÃO 4: ENCERRAMENTO
    # -----------------------------------------------------------------
    elif opcao == 4:
        print("Sistema encerrado com sucesso! Até a próxima.")
 
    # -----------------------------------------------------------------
    # Qualquer outra opção
    # -----------------------------------------------------------------
    else:
        print("Opção inválida! Digite um número de 1 a 4.")