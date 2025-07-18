print("bem vindo a simulação de sistema de compra!")

mercado_estoque = ["arroz" , "feijão" , "batata", "alface", "tomate"]
mercado_preço = 5.00, 4.00, 3.00, 2.00, 1.50
mercado_quantidade_minima = 80


while True:
    mercado_usuario = input("para escolher o arroz digite 1, para escolher o feijão digite 2, para escolher a batata digite 3 , para escolher a alface digite 4 e para escolher o tomate digite 5, ou digite 0 para encerrar a sua compra, ou digite 10 para mostrar os produtos disponiveis em estoque:")

    if mercado_usuario == "1":
        escolha = int(input("Arroz selecionado! Se quiser adicionar mais produtos digite 8, ou para ir para a forma de pagamento digite 7:"))
    elif mercado_usuario == "2":
        escolha = int(input("Feijão selecionado! Se quiser adicionar mais produtos digite 8, ou para ir para a forma de pagamento digite 7:"))
    elif mercado_usuario == "3":
        escolha = int(input("Batata selecionado! Se quiser adicionar mais produtos digite 8, ou para ir para a forma de pagamento digite 7:"))
    elif mercado_usuario == "4":
        escolha = int(input("Alface selecionado! Se quiser adicionar mais produtos digite 8, ou para ir para a forma de pagamento digite 7:"))
    elif mercado_usuario == "5":
        escolha = int(input("Tomate selecionado! Se quiser adicionar mais produtos digite 8, ou para ir para a forma de pagamento digite 7:"))

    elif mercado_usuario == "10":
        print("Produtos disponíveis em estoque:")
        for produto in mercado_estoque:
            print(mercado_estoque.index(produto) + 1, "-", produto)
        print("Quantidade mínima em estoque:", mercado_quantidade_minima)
        continue

    elif mercado_usuario == "0":
        print("saindo do atendimento....")
        break
    else:
        print("Opção inválida!")
        continue
    
    # Só chega aqui se escolha foi definida
    if escolha == 8:
        continue
    elif escolha == 7:
        print("Indo para a forma de pagamento...")
        while True:
            print("\nFormas de pagamento disponíveis:")
            print("1 - Dinheiro")
            print("2 - Cartão de crédito")
            print("3 - Cartão de débito")
            print("0 - Cancelar pagamento")
            pagamento = int(input("Escolha a forma de pagamento: "))
            if pagamento in [1, 2, 3]:
                print("Forma de pagamento selecionada.")
                total_produtos = int(input("Digite a quantidade total de produtos comprados: "))
                valor_total = float(input("Digite o valor total da compra (sem desconto): "))
                desconto = (total_produtos // 5) * 0.10  # 10% a cada 5 produtos
                if desconto > 0:
                    desconto_percentual = desconto * 100
                    if desconto_percentual > 100:
                        desconto_percentual = 100
                        desconto = 1.0
                    valor_com_desconto = valor_total * (1 - desconto)
                    print(f"Você ganhou {int(desconto_percentual)}% de desconto!")
                    print(f"Valor com desconto: R${valor_com_desconto:.2f}")
                else:
                    print("Sem desconto aplicado.")
                    valor_com_desconto = valor_total
                print(f"Pagamento de R${valor_com_desconto:.2f} realizado com sucesso!")
                break
            elif pagamento == 0:
                print("Pagamento cancelado. Voltando ao menu principal.")
                break
            else:
                print("Opção inválida, tente novamente.")
        break