# Durante uma reunião do grupo de pesquisa BIA/UFG, a equipe precisa simular o
# crescimento de um investimento com juros compostos. Usando o laço while, crie um programa que
# leia o valor inicial investido (capital), a taxa de juros mensal (%) e o valor alvo desejado. O
# programa deve calcular mês a mês o montante acumulado e exibir o extrato completo até que o
# capital atinja ou supere o valor alvo. Ao final, informe:
# • o número total de meses necessários para atingir o valor alvo;
# • o montante final acumulado;
# • o total de juros recebidos no período.
# Entrada: capital inicial (real), taxa de juros mensal (%), valor alvo (real).
# Saída: extrato mês a mês (mês, rendimento do período, montante acumulado) e total de meses
# necessários.

valorInicial = float(input("Capital inicial: "))
taxaJuros = (float(input("Taxa de juros: ")))/100
valorAlvo = float(input("Valor alvo: "))
auxValor = valorInicial
contMes = 0

while auxValor < valorAlvo:
    contMes += 1

    auxValor = (auxValor*taxaJuros) + auxValor

    print(f"Mes {contMes}: R$ {auxValor:.2f}")

print(f"\nMeses gastos: {contMes}")
print(f"Total de juros acumulados: R$ {auxValor - valorInicial:.2f}")
