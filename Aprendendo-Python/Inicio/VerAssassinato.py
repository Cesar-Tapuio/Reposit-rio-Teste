# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#   "Telefonou para a vítima?"
#   "Esteve no local do crime?"
#   "Mora perto da vítima?"
#   "Devia para a vítima?"
#   "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".


respostas = [False] * 5

print("0 - Não\n1 - Sim\n")

respostas[0] = bool(int(input("Telefonou para a vítima? ")))
respostas[1] = bool(int(input("Esteve no local do crime? ")))
respostas[2] = bool(int(input("Mora perto da vítima? ")))
respostas[3] = bool(int(input("Devia para a vítima? ")))
respostas[4] = bool(int(input("Já trabalhou com a vítima? ")))

contSim = respostas.count(True)

if contSim < 2:
    print("Inocente")

elif contSim == 2:
    print("Suspeito")

elif contSim == 3 or contSim == 4:
    print("Cumplice")

else:
    print("Culpado")



