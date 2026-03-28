# Durante uma atividade prática no laboratório da UFG, três colegas do BIA
# entregaram suas pontuações em um desafio de lógica. Faça um programa que leia
# três números inteiros e informe qual foi o maior e qual foi o menor valor digitado.
# Desafio extra: adaptar o programa para aceitar mais de três valores.
# Entrada: três números inteiros.
# Saída: maior e menor número.


quantidadeNumero = int(input("Digite quantos numeros serao lidos: "))
numeros = []

for i in range(quantidadeNumero):
    numeros.append(int(input(f"Numero {i+1}: ")))

numeros.sort()

print(f"O maior número é: {numeros[-1]}\nO menor número é: {numeros[0]}")