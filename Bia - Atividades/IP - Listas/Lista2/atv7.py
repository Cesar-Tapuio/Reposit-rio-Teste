# Um aluno do BIA/UFG está desenvolvendo um mini-jogo de adivinhação como projeto de
# introdução à programação. Usando o laço while, crie um programa que gere um número aleatório
# entre 1 e 100 (use o módulo random) e permita que o usuário tente adivinhar o número, com as
# seguintes dicas após cada tentativa:
# • "Muito baixo!" se o chute for menor que o número secreto;
# • "Muito alto!" se o chute for maior que o número secreto;
# • "Parabéns! Você acertou em X tentativas." ao acertar.
# Entrada: tentativas do usuário (números inteiros).
# Saída: dica após cada tentativa e mensagem de parabéns com o número de tentativas ao acertar

# randint(a, b) -> inteiro aleatório entre a e b (inclui os dois)
# random() -> número decimal entre 0.0 e 1.0
# uniform(a, b) -> número decimal entre a e b
# choice(lista) -> escolhe um item aleatório da lista
# shuffle(lista) -> embaralha os elementos da lista
# sample(range(a, b), k) -> sorteia k valores únicos no intervalo

import random

numero = random.randint(1, 100)
chute = (int(input("Chute um numero de 1 a 100: ")))
cont = 0
print(numero)

if chute == numero:
    print("Acertou de primeiraaa!!!!")

while chute != numero:
    cont += 1
    
    if chute < numero:
        print("Muito baixo!")
        chute = (int(input("Tente novamente: ")))
    
    elif chute > numero:
        print("Muito alto!")
        chute = (int(input("Tente novamente: ")))

if chute == numero:
    print(f"Parabéns! Você acertou em {cont} tentativas.")
        
    

