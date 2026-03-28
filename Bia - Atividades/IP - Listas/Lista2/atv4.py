# Durante uma aula de matemática computacional no BIA/UFG, o professor solicita um programa
# para exibir a tabuada. Utilize o laço for para criar um programa que leia um número inteiro N e
# exiba a tabuada completa desse número, de 1 a 10, formatada de forma clara.
# Desafio extra: permitir que o usuário escolha o intervalo da tabuada (ex.: de 1 a 20).
# Entrada: um número inteiro N.
# Saída: tabuada de N, de N×1 até N×10.


#Com while

# numeroTabuada = int(input("Numero desejado para tabuada: "))


# while 1:

#     inicioTabuada = int(input("Inicio da tabuada: "))
#     finalTabuada = int(input("Final tabuada: "))

#     if inicioTabuada < finalTabuada:

#         while inicioTabuada <= finalTabuada:
#             print(f"{numeroTabuada} x {inicioTabuada} = {numeroTabuada * inicioTabuada}")
#             inicioTabuada += 1
#         break

#     else:
#         print("O inicio da tabuada não pode ser maior que o final")


#Com For

numeroTabuada = int(input("Numero desejado para tabuada: "))

while 1:
    inicioTabuada = int(input("Inicio da tabuada: "))
    finalTabuada = int(input("Final da tabuada: "))

    if inicioTabuada <= finalTabuada:
        for i in range(inicioTabuada, finalTabuada + 1):
            print(f"{numeroTabuada} x {i} = {numeroTabuada * i}")
        break
    else:
        print("O inicio da tabuada não pode ser maior que o final")

