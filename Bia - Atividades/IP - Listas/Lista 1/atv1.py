#  Um estudante do BIA/UFG realizou duas avaliações em uma disciplina de
# programação. Desenvolva um programa que leia as duas notas, calcule a média
# final e exiba:
# • “Aprovado com Distinção”, se a média for exatamente 10;
# • “Aprovado”, se a média for maior ou igual a 7 e menor que 10;
# • “Reprovado”, se a média for menor que 7.
# Entrada: duas notas reais.
# Saída: média e situação final do aluno.

nota=0
for i in range(2):
    
    nota += int(input(f"Digite a nota {i+1}: "))

media = float(nota/2)

if media == 10:
    print(f"Media: {media} - Aprovado com Distinção")

elif media >= 7 and media < 10:
    print(f"Media: {media} - Aprovado")

elif media < 7:
    print(f"Media: {media} - Reprovado")