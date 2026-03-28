# Um pesquisador vinculado ao CEIA deseja simular como seria se ele recebesse
# como um profissional de mercado, com salário líquido do mês em comparação ao
# seu recebimento de bolsa (isenta de tributos). Desenvolva um programa que leia o
# valor da hora trabalhada e a quantidade de horas no mês, calcule o salário bruto e
# depois aplique os descontos:
# IR
# até R$ 1.900,00 → isento
# de R$ 1.900,01 até R$ 2.800,00 → 7,5%
# de R$ 2.800,01 até R$ 3.700,00 → 15%
# acima de R$ 3.700,00 → 20%
# INSS → 10%
# Ao final, mostrar:
# • salário bruto,
# • valor do IR,
# • valor do INSS,
# • salário líquido.
# • Comparação com o valor da bolsa (ISENTA)
# Entrada: valor da hora e quantidade de horas do salário proposto, e valor da bolsa
# atual para análise.
# Saída: folha de pagamento resumida e comparação.

valorHora = float(input("Valor da hora trabalhada: "))
horaTrabalhada = int(input("Horas trabalhadas: "))
valorBolsa = float(input("Valor da bolsa: "))
salarioBruto = valorHora * horaTrabalhada


if salarioBruto <= 1900:
    print(f"\nSalario Bruto de {salarioBruto}\nIsento de IR\nINSS de 10%: R$ -{salarioBruto*0.1}\nSalario liquido: R$ {salarioBruto-(salarioBruto*0.1)}")
    
    if salarioBruto-(salarioBruto*0.1) > valorBolsa:
        print(f"Salario liquido é R$ {(salarioBruto-(salarioBruto*0.1)) - valorBolsa} maior que a bolsa")

    else:
        print(f"Salario liquido é R$ {valorBolsa - (salarioBruto-(salarioBruto*0.1))} menor que a bolsa")


elif salarioBruto > 1900 and salarioBruto <= 2800:
    print(f"\nSalario Bruto de {salarioBruto}\nIR de 7,5%: R$ -{salarioBruto*0.075}\nINSS de 10%: R$ -{salarioBruto*0.1}\nSalario liquido: R$ {salarioBruto-(salarioBruto*0.175)}") #0.10 de INSS e 0.075 de IR, por isso 0.175
    
    if salarioBruto-(salarioBruto*0.175) > valorBolsa:
        print(f"Salario liquido é R$ {(salarioBruto-(salarioBruto*0.175)) - valorBolsa} maior que a bolsa")

    else:
        print(f"Salario liquido é R$ {valorBolsa - (salarioBruto-(salarioBruto*0.175))} menor que a bolsa")


elif salarioBruto > 2800 and salarioBruto <= 3700:
    print(f"\nSalario Bruto de {salarioBruto}\nIR de 15%: R$ -{salarioBruto*0.15}\nINSS de 10%: R$ -{salarioBruto*0.1}\nSalario liquido: R$ {salarioBruto-(salarioBruto*0.25)}")

    if salarioBruto-(salarioBruto*0.25) > valorBolsa:
        print(f"Salario liquido é R$ {(salarioBruto-(salarioBruto*0.25)) - valorBolsa} maior que a bolsa")

    else:
        print(f"Salario liquido é R$ {valorBolsa - (salarioBruto-(salarioBruto*0.25))} menor que a bolsa")


elif salarioBruto > 3700:
    print(f"\nSalario Bruto de {salarioBruto}\nIR de 20%: R$ -{salarioBruto*0.2}\nINSS de 10%: R$ -{salarioBruto*0.1}\nSalario liquido: R$ {salarioBruto-(salarioBruto*0.30)}")

    if salarioBruto-(salarioBruto*0.3) > valorBolsa:
        print(f"Salario liquido é R$ {(salarioBruto-(salarioBruto*0.3)) - valorBolsa} maior que a bolsa")

    else:
        print(f"Salario liquido é R$ {valorBolsa - (salarioBruto-(salarioBruto*0.3))} menor que a bolsa")

