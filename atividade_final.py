def venda_de_produto():
    print("******venda de produto******")
    try:
        nome_produto = input("Informe o nome do produto: ")

        preco_unitario = float(input("Informe o preço unitário do produto: R$ "))

        quantidade = int(input("Informe a quantidade a ser vendida: "))

    except ValueError:
        print("Os campos 'quantidade' e 'preço' devem conter apenas valores numéricos.")
        return

    valor_total = preco_unitario * quantidade

    print(f"Valor a pagar R$: {valor_total:.2f}")

    print("Escolha o método de pagamento:1.dinheiro 2.pix 3.cartão(crédito/débito)")

    pagamento = input("Informe o número correspondente ao método de pagamento: ")

    if pagamento == '1':
        print("Você escolheu dinheiro. pagamento realizado no dinheiro")
    elif pagamento == '2':
        print("Você escolheu pix. pagamento realizado no pix")
    elif pagamento == '3':
        print("Você escolheu cartão. pagamento realizado no cartão(crédito/débito)")
    else:
        print("Método de pagamento inválido, escolha outra opção.")
        return

    print("obrigado por comprar, volte sempre")

venda_de_produto()