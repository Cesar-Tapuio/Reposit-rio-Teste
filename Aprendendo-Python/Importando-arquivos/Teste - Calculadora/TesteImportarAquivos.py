numeros = []
soma = 0

with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Teste - Calculadora/input.txt", "r") as arquivo:
    for linha in arquivo:
        numeros.append(int(linha.strip()))

for numero in numeros:
    soma += numero

print(f"A soma dos números é: {soma}")