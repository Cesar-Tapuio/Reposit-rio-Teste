
nome = 'cesar'
email = '@'
senha = '123'
cpf = '123'

with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{senha},{cpf}\n")