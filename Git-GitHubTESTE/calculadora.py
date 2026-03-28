numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operador = input("Digite a operação (+, -, *, /): ")

if operador == "+":
    resultado = numero1 + numero2
    print("O resultado da adição é:", resultado)


elif operador == "-":
    resultado = numero1 - numero2
    print("O resultado da subtração é:", resultado)

elif operador == "*":
    resultado = numero1 * numero2
    print("O resultado da multiplicação é:", resultado)

elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")