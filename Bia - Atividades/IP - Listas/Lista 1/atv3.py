# O CEIA/UFG está simulando reajustes salariais para colaboradores de um projeto.
# Crie um programa que leia o salário atual e calcule o novo salário com base
# nestas regras:
# até R$ 1.500,00 → aumento de 20%
# de R$ 1.500,01 até R$ 3.000,00 → aumento de 10%
# acima de R$ 3.000,00 → aumento de 5%
# O programa deve exibir:
# • salário antes do reajuste,
# • percentual aplicado,
# • valor do aumento,
# • novo salário.
# Entrada: salário atual.
# Saída: detalhamento do reajuste

quantidadeSalarios = int(input("Digite quantos salarios serão reajustados: "))
salario = []
salarioReajustado = []

for i in range(quantidadeSalarios):
    salario.append(float(input(f"Digite o salario numero {i+1}: ")))
    
    if salario[i] <= 1500:
        salarioReajustado.append(salario[i]+(salario[i]*0.2))

    elif salario[i] > 1500 and salario[i] <= 3000:
        salarioReajustado.append(salario[i]+(salario[i]*0.1))

    elif salario[i] > 3000:
        salarioReajustado.append(salario[i]+(salario[i]*0.05))

for i in range(quantidadeSalarios):
    print(f"Salario numero {i+1}: \nSalario antigo: {salario[i]}\nSalario reajustado: {salarioReajustado[i]}\n")


