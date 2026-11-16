# SYSTEMA PDV E CAIXA - VERSAO APRIMORADA   
saldo = 2500.00
total_vendas = 0
total_despesas = 0.0
cliente_comum = 0
cliente_vip = 0

print("\n" + "=" * 50)
print("SISTEMA DE CAIXA DA LOJA")
print("\n" + "=" * 50)

opcao = 0
for opcao in range(1, 5):
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1 - Processar Venda de Cliente Comum")
    print("2 - Processar Venda de Cliente VIP / Aluno")
    print("3 - Imprimir Relatório e Extrato")
    print("4 - Encerrar Expediente")
    opcao = input("Digite a opção desejada: ").strip()


    if opcao =="1":
        print("\n--- NOVA VENDA: CLIENTE COMUM ---")
        nome = input("Nome do cliente: ")
        quantidade = int(input("Quantidade de itens: "))
        valor = float(input("Valor unitário do item: R$ "))
        total = quantidade * valor

        # Desconto de quantidade
        if quantidade >= 10:
            desconto = total * 0.10
            total -= desconto
            print("Desconto de 10% aplicado por quantidade!")
        elif quantidade >= 5:
            desconto = total * 0.05
            total -= desconto
            print("Desconto de 5% aplicado por quantidade!")

        # Imposto fixo
        imposto = total * 0.02
        total += imposto

        # Pagamento
        print(f"Total a pagar: R$ {total:.2f}")
        pagamento = float(input("Valor pago pelo cliente: R$ "))
        if pagamento >= total:
            troco = pagamento - total
            saldo += total
            total_vendas = total_vendas + 1
            total_despesas = total_despesas + total
            cliente_comum = cliente_comum + 1
            print(f"Venda realizada com sucesso! Troco: R$ {troco:.2f}")
        else:
            print("Venda cancelada: Valor pago é menor que o total.")

    elif opcao == "2":
        print("\n--- NOVA VENDA: CLIENTE VIP / ALUNO ---")
        nome_vip = input("Nome do cliente VIP: ")
        quantidade = int(input("Quantidade de itens: "))
        valor = float(input("Valor unitário do item: R$ "))
        total = quantidade * valor

        # Desconto de quantidade
        if quantidade >= 10:
            desconto_quantidade = total * 0.10
            total -= desconto_quantidade
            print("Desconto de 10% aplicado por quantidade!")
        elif quantidade >= 5:
            desconto = total * 0.05
            total -= desconto
            print("Desconto de 5% aplicado por quantidade!")

        # Desconto extra VIP de 15%
        desconto_vip = total * 0.15
        total -= desconto_vip
        print("Desconto VIP especial de 15% aplicado!")


        # Pagamento
        print(f"Total a pagar (com desconto VIP): R$ {total:.2f}")
        pagamento = float(input("Valor pago pelo cliente: R$ "))
        if pagamento >= total:
            troco = pagamento - total
            saldo = saldo + total
            total_vendas = total_vendas + 1
            total_despesas = total_despesas + total
            cliente_vip = cliente_vip + 1
            print(f"Venda VIP realizada com sucesso! Troco: R$ {troco:.2f}")
        else:
            print("Venda cancelada: Valor pago é menor que o total.")

    elif opcao == "3":
        print("\n" + "=" * 50)
        print("RELATÓRIO CONSOLIDADO DO CAIXA")
        print("\n" + "=" * 50)
        print(f"Saldo final no caixa: R$ {saldo:.2f}")
        print("Total de vendas realizadas:", total_vendas)
        print(f"Total faturado no dia: R$ {total_despesas:.2f}")
        print("Atendimentos Cliente Comum:", cliente_comum)
        print("Atendimentos Cliente VIP:", cliente_vip)
        if saldo < 1000.00:
            print("ALERTA: Saldo em caixa abaixo do limite de segurança!")
        print("\n" + "=" * 50)

    elif opcao == "4":
        print("Encerrando o sistema e fechando o caixa...")
    else:
        print("Opção inválida! Digite uma opção de 1 a 4.")