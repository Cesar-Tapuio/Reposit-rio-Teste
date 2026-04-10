import numpy as np

x = np.loadtxt("/home/cesar/Documents/Python - Testes/Aprendendo/Bia - Atividades/Aulas/dadosBIA/notas_alunos_1000_4_bimestres.csv", delimiter=",")

y = np.loadtxt("/home/cesar/Documents/Python - Testes/Aprendendo/Bia - Atividades/Aulas/dadosBIA/notas_alunos_10000_5_avaliacoes_media63.csv", delimiter=",")

x_y = x.view()

x_y = x_y[:,1:]

print(x_y.shape)
print(f"{np.sum(x_y/len(x_y)/4):.2f}")
print(f"Media: {np.mean(x_y):.2f}")
print(f"Desvio Padrão: {np.std(x_y):.2f}")
print(f"Variância: {np.var(x_y):.2f}")
print(f"Mínimo: {np.min(x_y):.2f}")
print(f"Máximo: {np.max(x_y):.2f}")

print("Media por bimestre:")
for i in range(4):
    print(f"Bimestre {i+1}: {np.mean(x_y[:,i]):.2f}")

