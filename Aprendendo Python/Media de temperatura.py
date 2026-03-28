# Exercício 13 da seção de listas da Python Brasil:
# https://wiki.python.org.br/ExerciciosListas

# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule e MOSTRE A MÉDIA ANUAL das temperaturas e MOSTRE TODAS AS TEMPERATURAS ACIMA DA MÉDIA ANUAL,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

# -as temperaturas só serão dadas em inteiro
# -todos os meses do ano serão passados à funçao, começando de janeiro e terminando em dezembro.
#  Todos seguidos de sua temperatura mensal

# (Funçoês recomendadas para estudo:
#     - .ljust()
#     - enumerate()
#     - sum()
#     - len()


#     >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '30']
#     >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
#     >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
#     Média anual: 24.75 Graus
#      1 - Janeiro:       30°
#      2 - Fevereiro:     33°
#      3 - Março:         27°
#      4 - Abril:         25°
#      5 - Maio:          29°
#      6 - Junho:         25°
#     11 - Novembro:      33°
#     12 - Dezembro:      25°
#     >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '35']
#     >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
#     >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
#     Média anual: 25.17 Graus
#      1 - Janeiro:       35°
#      2 - Fevereiro:     33°
#      3 - Março:         27°
#      5 - Maio:          29°
#     11 - Novembro:      33°

# """


# def temperaturas_acima_da_media():
#     """Escreva aqui sua solução: """

# Resposta simples ->

# meses = []
# tempTotal = 0

# for i in range(12):
#     mesTemp = int(input(f"Temperatura do mês {i+1}: "))
#     tempTotal += mesTemp

# print("Media de temperatura anual é de", tempTotal//12)

#Resposta media

# meses = []
# tempTotal = 0

# numeroMeses = int(input("Digite o numero de meses que quer calcular: "))

# for i in range(numeroMeses):
#     mesTemp = int(input(f"Temperatura do mes {i+1}: "))
#     tempTotal += mesTemp

# print("Media de temperatura anual é de", tempTotal//numeroMeses)

#Resposta complexa

tempMesGeral = []


def verificarMes (x):


    if x == 1:
        return "janeiro"
    elif x == 2:
        return "fevereiro"
    elif x == 3:
        return "março"
    elif x == 4:
        return "abril"
    elif x == 5:
        return "maio"
    elif x == 6:
        return "junho"
    elif x == 7:
        return "julho"
    elif x == 8:
        return "agosto"
    elif x == 9:
        return "setembro"
    elif x == 10:
        return "outubro"
    elif x == 11:
        return "novembro"
    elif x == 12:
        return "dezembro"

def addTempEspecifico():
    
    print("\nDigite o numero do mes que deseja adicionar uma temperatura: ")
    mesEscolhido = int(input())

    print(f"\n O mes escolhido foi {verificarMes(mesEscolhido)}")


def menuPrincipal():

    print("Adicionar temperatura de um mes especifico - 1")
    print("Adicionar temperatura de mai de um mes - 2")
    print("Verificar temperatura de um mes especifico - 3")
    print("Verificar media de temperatura de meses especificos - 4")
    print("Calcular media total de temperatura - 5\n")

    opcaoMenu = int(input("Digite a opcao escolhida: "))

    if opcaoMenu == 1:
        addTempEspecifico()

menuPrincipal()



