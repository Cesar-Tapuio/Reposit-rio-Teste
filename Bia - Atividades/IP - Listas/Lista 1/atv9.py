#  Durante uma atividade no laboratório da UFG, um sistema apresentou falha e a
# equipe do BIA/CEIA precisa fazer uma triagem inicial para entender a gravidade do
# problema. Desenvolva um programa que faça 5 perguntas com respostas sim ou
# não:
# a. O sistema parou de responder?
# b. Houve perda de dados?
# c. O problema afetou mais de um usuário?
# d. O erro ocorreu mais de uma vez no mesmo dia?
# e. Foi necessário interromper uma atividade importante?
# Com base na quantidade de respostas positivas, o programa deve classificar o
# incidente como:
# • Sem indícios de criticidade → 0 ou 1 resposta positiva
# • Baixa criticidade → 2 respostas positivas
# • Média criticidade → 3 ou 4 respostas positivas
# • Alta criticidade → 5 respostas positivas
# Entrada: cinco respostas (sim/não).
# Saída: classificação final do incidente.

respostas = []
contSim = 0

respostas.append(input("O sistema parou de responder?"))
respostas.append(input("Houve perda de dados?"))
respostas.append(input("O problema afetou mais de um usuário?"))
respostas.append(input("O erro ocorreu mais de uma vez no mesmo dia?"))
respostas.append(input("Foi necessário interromper uma atividade importante?"))

for resposta in respostas:
    if resposta.lower() == "sim":
        contSim += 1

if contSim == 0 or contSim == 1:
    print("Sem indícios de criticidade")

elif contSim == 2:
    print("Baixa criticidade")

elif contSim == 3 or contSim == 4:
    print("Média criticidade")

elif contSim == 5:
    print("Alta criticidade")
