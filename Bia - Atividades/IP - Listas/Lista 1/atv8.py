# Em uma atividade interdisciplinar entre programação e raciocínio lógico no CEIA,
# os alunos precisam verificar se três segmentos podem formar um triângulo. Crie
# um programa que leia três valores e verifique se eles podem formar um triângulo;
# caso possam, classifique-o como:
# Equilátero: três lados iguais;
# Isósceles: dois lados iguais;
# Escaleno: três lados diferentes.
# Entrada: três valores reais.
# Saída: mensagem informando se forma triângulo e sua classificação.

lado = []

for i in range(3):

    lado.append(float(input(f"Digite o valor do lado {i+1}: ")))

lado.sort()

if lado[0] == lado[1] and lado[1] == lado[2]:
    print("Equilátero: três lados iguais")


elif lado[0] == lado[1] or lado[1] == lado[2]:
    print("Isósceles: dois lados iguais")

else:
    print("Escaleno: três lados diferentes")

