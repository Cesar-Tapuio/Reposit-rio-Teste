# Um aluno do BIA precisa calcular a média de notas de uma turma sem saber de antemão
# quantas notas serão inseridas. Desenvolva um programa que leia notas repetidamente utilizando o
# laço while, encerrando a entrada quando o usuário digitar -1 (sentinela). Ao final, o programa deve
# exibir a média das notas inseridas, a maior e a menor nota da turma.
# Desafio extra: exibir também quantas notas ficaram acima da média.
# Entrada: notas reais digitadas uma a uma; -1 para encerrar.
# Saída: quantidade de notas, média, maior nota e menor nota.

notas = []
i=0
cont = 0
notasTotais = 0

while 1:
    notas.append(int(input(f"Nota do aluno numero {cont+1}: ")))

    if notas[-1] == -1:
        break
    else:
        notasTotais += notas[cont]
        cont += 1


print(f"Media de notas: {notasTotais/cont}")


