# Durante uma aula de Python no BIA/UFG, foi proposto criar uma calculadora
# simples. Desenvolva um programa que leia dois números e depois solicite ao
# usuário a operação desejada:
# • soma
# • subtração
# • multiplicação
# • divisão
# O programa deve exibir o resultado da operação escolhida.
# Entrada: dois números e a operação.
# Saída: resultado calculado.

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))

print('Digite "+" para soma')
print('Digite "-" para subtração')
print('Digite "/" para divisão')
print('Digite "*" para multiplicação')

operacao = input()

if operacao == "+":
    print(f"Resultado da soma: {num1+num2}")

elif operacao == "-":
    print(f"Resultado da subtração: {num1-num2}")

elif operacao == "/":
    print(f"Resultado da divisão: {num1/num2}")

elif operacao == "*":
    print(f"Resultado da multiplicação: {num1*num2}")