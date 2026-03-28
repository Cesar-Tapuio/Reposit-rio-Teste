# Em uma atividade de análise de dados no laboratório do BIA, os alunos precisam verificar quais
# números de uma sequência são primos. Utilizando o laço for, escreva um programa que leia um
# número inteiro N e liste todos os números primos de 2 até N.
# Dica: um número é primo se for divisível apenas por 1 e por ele mesmo. Utilize um laço for
# interno para verificar os divisores.
# Entrada: um número inteiro positivo N.
# Saída: lista de todos os números primos entre 2 e N e a quantidade total encontrada.

n = int(input("Digite um número inteiro positivo: "))

quantidade = 0

print(f"Números primos entre 2 e {n}:")

for num in range(2, n + 1):
    e_primo = True

    for i in range(2, num):
        if num % i == 0:
            e_primo = False
            break

    if e_primo:
        print(num, end=" ")
        quantidade += 1

print("\nQuantidade total de números primos:", quantidade)

