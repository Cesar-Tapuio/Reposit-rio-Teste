
def cadastrarProd():
    estoque = {}
    qtd = int(input("Quantos produtos deseja cadastrar? "))
    for i in range(qtd):
        nome = input("\nNome do produto: ")
        unidade = input("Tipo de unidade: ")
        quantidade_inicial = float(input("Quantidade inicial: "))
        consumo_diario = float(input("Consumo médio por dia: "))
        prazo_reposicao = int(input("Prazo de reposição (dias): "))

        estoque[nome] = {
            "unidade": unidade,
            "saldo": quantidade_inicial,
            "saldo_inicial": quantidade_inicial,
            "consumo": consumo_diario,
            "prazo": prazo_reposicao,
            "lotes": [(quantidade_inicial, 0)],
            "total_saidas": 0
        }

    return estoque

def registrar(estoque):
    total = int(input("\nQuantas movimentações serão registradas? "))
    for i in range(total):
        nome = input("\nProduto: ")
        tipo = input("Movimentação (ENTRADA/SAIDA): ").upper()
        quantidade = float(input("Quantidade: "))
        preco = float(input("Preço unitário: "))

        if nome not in estoque:
            print("Produto não encontrado")

        prod = estoque[nome]

        if tipo == "ENTRADA":
            prod["saldo"] += quantidade
            prod["lotes"].append((quantidade, preco))

        elif tipo == "SAIDA":
            if prod["saldo"] < quantidade:
                print("Erro: estoque insuficiente")



            prod["saldo"] -= quantidade
            prod["total_saidas"] += quantidade

            restante = quantidade
            novos_lotes = []

            for qtd_lote, valor_lote in prod["lotes"]:
                if restante == 0:
                    novos_lotes.append((qtd_lote, valor_lote))
                elif qtd_lote <= restante:
                    restante -= qtd_lote

                else:
                    novos_lotes.append((qtd_lote - restante, valor_lote))
                    restante = 0

            prod["lotes"] = novos_lotes



def calcTotal(lotes):
    soma = 0
    for qtd, valor in lotes:
        soma += qtd * valor
    return soma



def relatorio(estoque):
    print("\nRelatório de estoque:")

    maior_saida_nome = ""
    maior_saida_valor = 0

    for nome, prod in estoque.items():
        saldo = prod["saldo"]
        valor_total = calcTotal(prod["lotes"])
        ponto_reposicao = prod["consumo"] * prod["prazo"]
        situacao = "REPOR" if saldo < ponto_reposicao else "OK"

        if prod["total_saidas"] > maior_saida_valor:
            maior_saida_nome = nome
            maior_saida_valor = prod["total_saidas"]

        if saldo > prod["saldo_inicial"]:
            status = "Aumentou"
        elif saldo < prod["saldo_inicial"]:
            status = "Diminuiu"
        else:
            status = "Estável"

        print(f"\nProduto: {nome}")
        print(f"Saldo atual: {saldo}")
        print(f"Valor total em estoque: {valor_total:.2f}")
        print(f"Ponto de reposição: {ponto_reposicao}")
        print(f"Situação: {situacao}")
        print(f"Comparação: {status}")

    print(f"\nProduto com maior saída: {maior_saida_nome}")





estoque = cadastrarProd()
registrar(estoque)
relatorio(estoque)