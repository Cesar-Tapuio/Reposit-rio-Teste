# A partir de uma simulação de lançamento de dados, foram armazenados os valores de cada lançamento.
# Mostre na tela:
# 1)Quantas vezes o dado foi lançado;
# 2)Quantas vezes cada valor foi obtido;
# 3)Qual lado caiu mais vezes (e quantas vezes.)

#     >>> lancar_dados(2, 2, 2, 5, 3, 3, 1, 3, 4, 2, 6, 4, 3, 4, 4, 2, 6, 3, 6, 3, 4,
#     ... 3, 5, 5, 5, 1, 2, 1, 6, 5, 6, 3, 1, 6, 1, 1, 6, 5, 1, 6, 1, 1, 2, 1, 1, 2, 2,
#     ... 4, 4, 4, 2, 1, 4, 6, 6, 4, 2, 4, 4, 2, 5, 3, 6, 1, 2, 5, 4, 4, 5, 3, 4, 6, 6)
#     O dado foi lançado 73 vezes
#     O número 1 caiu 13 vezes
#     O número 2 caiu 13 vezes
#     O número 3 caiu 10 vezes
#     O número 4 caiu 15 vezes
#     O número 5 caiu 9 vezes
#     O número 6 caiu 13 vezes
#     O lado com o número 4 caiu mais vezes (15 vezes)


nDado = []
maisLanc = []

nLancamento = int(input("Digite quantas vezes o dado foi lançado \n"))

for i in range(nLancamento):
    numeroAtual = int(input(f"Numero do lançamento n {i+1} \n"))
    nDado.append(numeroAtual)

print(f"O dado foi lançado {len(nDado)} vezes")

print(f"O numero 1 aparece {nDado.count(1)} vezes")

print(f"O numero 2 aparece {nDado.count(2)} vezes")

print(f"O numero 3 aparece {nDado.count(3)} vezes")

print(f"O numero 4 aparece {nDado.count(4)} vezes")

print(f"O numero 5 aparece {nDado.count(5)} vezes")

print(f"O numero 6 aparece {nDado.count(6)} vezes")







