# Um pesquisador do CEIA/UFG coletou dados de temperatura (em °C) ao longo de 7 dias
# consecutivos em um experimento de IoT com sensores ESP32. Utilizando o laço for, crie um
# programa que leia as 7 temperaturas e calcule e exiba:
# • a média das temperaturas;
# • o dia (1 a 7) em que ocorreu a maior temperatura;
# • o dia (1 a 7) em que ocorreu a menor temperatura.
# Entrada: sete valores reais de temperatura.
# Saída: temperatura média, maior e menor temperatura registrada nos 7 dias.

temperaturas = []
aux = 0

for i in range(7):
    temperaturas.append(int(input(f"Temperatura do dia {i+1}: ")))
    aux += temperaturas[i]

temperaturas.sort()

print(f"Menor temperatura: {temperaturas[0]}°C")
print(f"Maior temperatura: {temperaturas[-1]}°C")
print(f"Temperatura media: {aux/7:.2f}°C")