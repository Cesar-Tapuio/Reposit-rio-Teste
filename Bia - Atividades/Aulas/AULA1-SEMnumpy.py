
#5 dados, [0] = numero do aluno, de [1] a [4] são as notas

#Fazer Media, Min, Max

medias = [0, 0, 0, 0]
qntdAluno = 1000

#Medias:

with open("/home/cesar/Documents/Python - Testes/Aprendendo/Bia - Atividades/Aulas/dadosBIA/notas_alunos_1000_4_bimestres.csv", "r" ) as dados:
    for dado in dados:
        medias[0] += float(dado.strip().split(",")[1])
        medias[1] += float(dado.strip().split(",")[2])
        medias[2] += float(dado.strip().split(",")[3])
        medias[3] += float(dado.strip().split(",")[4])

        


for i in range(4):
    print(f"Media do bimestre {i+1}: {medias[i]/qntdAluno:.2f}")

#Nota Min e Max:

min_nota = float("inf")
max_nota = float("-inf")

with open("/home/cesar/Documents/Python - Testes/Aprendendo/Bia - Atividades/Aulas/dadosBIA/notas_alunos_1000_4_bimestres.csv", "r") as dados:
    for linha in dados:
        valores = linha.strip().split(",")

        # ignora a primeira coluna (ID)
        notas = list(map(float, valores[1:]))

        for nota in notas:
            if nota < min_nota:
                min_nota = nota
            if nota > max_nota:
                max_nota = nota

print(f"Mínimo: {min_nota}")
print(f"Máximo: {max_nota}")
