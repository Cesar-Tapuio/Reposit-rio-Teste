# Durante as aulas de programação no BIA/UFG, o professor desafia os alunos a criar um
# contador simples. Escreva um programa que utilize o laço while para exibir na tela todos os
# números inteiros de 1 até N, onde N é fornecido pelo usuário. O programa deve também calcular e
# exibir a soma de todos os números do intervalo.
# Entrada: um número inteiro positivo N.
# Saída: números de 1 a N (um por linha) e a soma total.

num = int(input("Digite um numero: "))
cont = 0
somaTotal = 0

while cont < num:
    cont += 1
    somaTotal += cont
    print(cont)
print(f"Soma total: {somaTotal}")

