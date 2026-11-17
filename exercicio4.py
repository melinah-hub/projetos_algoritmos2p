# SYSTEMA PDV E CAIXA - VERSAO APRIMORADA   
saldo = 10.00
total_vendas = 0
faturamento_total = 0.00
cliente_comum = 0
cliente_vip = 0
cliente_funcional = 0

print("\n" + "=" * 50)
print("SISTEMA DE CAIXA DA LOJA")
print("\n" + "=" * 50)

opcao = 0
while opcao != "5":
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1 - Processar Venda de Cliente Comum")
    print("2 - Processar Venda de Cliente VIP / Aluno")
    print("3 - Processar Venda de Funcional/Professor")
    print("4- Imprimir Relatório e Extrato")
    print("5- Encerrar Expediente")
    opcao = (input("Digite a opção desejada: "))


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

        if quantidade > 3:
            total += 1.50
            print("Taxa de embalagem ecológica: + R$ 1.50")

        # Imposto fixo
        imposto = total * 0.02
        total += imposto

        # Pagamento
        print(f"Total a pagar: R$ {total:.2f}")
        pagamento = float(input("Valor pago pelo cliente: R$ "))
        if pagamento >= total:
            troco = pagamento - total
            if saldo>= troco:
                saldo += total
                total_vendas = total_vendas + 1
                faturamento_total += total
                cliente_comum = cliente_comum + 1
                print(f"Venda realizada com sucesso! Troco: R$ {troco:.2f}")
            else:
                print("Venda cancelada: Caixa com saldo insuficiente para fornecer o troco.")
       
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


        if quantidade > 3:
            total += 1.50
            print("Taxa de embalagem ecológica: + R$ 1.50")
        # Imposto fixo
        imposto = total * 0.02
        total += imposto


        # Pagamento
        print(f"Total a pagar (com desconto VIP): R$ {total:.2f}")
        pagamento = float(input("Valor pago pelo cliente: R$ "))
        if pagamento >= total:
            troco = pagamento - total
            if saldo >= troco:
                saldo += total
                total_vendas += 1
                faturamento_total += total
                cliente_vip += 1
                print(f"Venda VIP realizada com sucesso! Troco: R$ {troco:.2f}")
            else:
                print("Venda cancelada: Caixa com saldo insuficiente para fornecer o troco.")
        else:
            print("Venda cancelada: Valor pago é menor que o total.")
       
    elif opcao == "3":
        print("\n--- NOVA VENDA: FUNCIONAL/PROFESSOR---")
        nome_funcional = input("Nome do funcionário/professor: ")
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

        # Desconto extra para funcionários/professores de 20%
        desconto_funcional = total * 0.20
        total -= desconto_funcional
        print("Desconto funcional de 20% aplicado!")

        if quantidade > 3:
            total += 1.50
            print("Taxa de embalagem ecológica: + R$ 1.50")

        # Pagamento
        print(f"Total a pagar (com desconto funcional): R$ {total:.2f}")
        pagamento = float(input("Valor pago pelo cliente: R$ "))
        if pagamento >= total:
            troco = pagamento - total
            if saldo >= troco:
                saldo +=total
                total_vendas +=1
                faturamento_total += total
                cliente_funcional += 1
                print(f"Venda funcional realizada com sucesso! Troco: R$ {troco:.2f}")
            else:
                print("Venda cancelada: Caixa com saldo insuficiente para fornecer o troco.")
        else:
            print("Venda cancelada: Valor pago é menor que o total.")

    elif opcao == "4":
        print("\n" + "=" * 50)
        print("RELATÓRIO CONSOLIDADO DO CAIXA")
        print("\n" + "=" * 50)
        print(f"Saldo final no caixa: R$ {saldo:.2f}")
        print("Total de vendas realizadas:", total_vendas)
        print(f"Total faturado no dia: R$ {faturamento_total:.2f}")
        print("Atendimentos Cliente Comum:", cliente_comum)
        print("Atendimentos Cliente VIP:", cliente_vip)
        print("Atendimentos Funcional/Professor:", cliente_funcional)
        if saldo < 1000.00:
            print("ALERTA: Saldo em caixa abaixo do limite de segurança!")
        print("\n" + "=" * 50)

    elif opcao == "5":
        print("Encerrando o sistema e fechando o caixa...")
    else:
        print("Opção inválida! Digite uma opção de 1 a 5.")