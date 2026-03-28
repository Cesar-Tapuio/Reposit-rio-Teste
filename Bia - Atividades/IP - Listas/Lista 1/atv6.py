# Um aluno da UFG que participa de reuniões do CEIA quer calcular o valor de sua
# conta de celular com base nos minutos utilizados no mês. Faça um programa que
# leia a quantidade de minutos e calcule o valor a pagar com a seguinte tabela:
# até 100 minutos → R$ 0,20 por minuto
# de 101 até 200 minutos → R$ 0,18 por minuto
# acima de 200 minutos → R$ 0,15 por minuto
# Entrada: quantidade de minutos consumidos.
# Saída: valor total da conta.


minutosUtilizados = float(input("Digite a quantidade de minutos utilizados: "))

if minutosUtilizados <= 100:
    valorTotal = minutosUtilizados*0.2

elif minutosUtilizados <= 200:
    valorTotal = minutosUtilizados*0.18

elif minutosUtilizados > 200:
    valorTotal = minutosUtilizados*0.15

print(f"Valor total da conta é: R$ {valorTotal}")
