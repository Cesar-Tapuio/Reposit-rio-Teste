#  Um colega do BIA foi até um caixa eletrônico próximo à UFG para sacar dinheiro
# antes do intervalo. Crie um programa que leia o valor desejado para saque e
# informe a menor quantidade possível de cédulas para entregar o valor exato,
# considerando notas de:
# • R$ 100
# • R$ 50
# • R$ 10
# • R$ 5
# • R$ 1
# Entrada: valor inteiro do saque.
# Saída: quantidade de cada nota utilizada.

valor = float(input("Digite o valor a ser sacado: "))

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas1 = valor

print(f"Notas de 100: {int(notas100)}")
print(f"Notas de 50: {int(notas50)}")
print(f"Notas de 10: {int(notas10)}")
print(f"Notas de 5: {int(notas5)}")
print(f"Moedas de 1: {int(notas1)}")

