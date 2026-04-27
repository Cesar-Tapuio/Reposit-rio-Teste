

def avaliar(n):
    if n in (0, 1):
        return "INDEF", None

    for i in range(2, n):
        if n % i == 0:
            return "SAFE", i

    return "MINA", None


while True:

    entrada = input("Digite um número ou 'sair' -> ")

    if entrada.lower() == "sair":  
        break
    try:
        n = int(entrada)
        status, valor = avaliar(n)
        print(f"CELULA {n} :: STATUS={status} :: PAYLOAD={valor}")
    except:
        print("Entrada invalida ")