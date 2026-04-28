

def cadastro():
    print("Cadastro de usuário")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Teste - Login/usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{senha}\n")

    print(f"Usuário {nome} cadastrado com sucesso!")




def login():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    dados = []
    aux = False
    
    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Teste - Login/usuarios.txt", "r") as arquivo:
        #Procurar resgistros do usuario
        for dado in arquivo:
            if dado.strip().split(",")[0] == nome:
                if dado.strip().split(",")[2] == senha:
                    print("\nLogin feito com sucesso!")
                    aux = True
                    break

    if aux == False:
        print("\nUsuário ou senha incorretos!")
                
            



def menu():
    while True:
        
        print("\n1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastro()
        elif escolha == "2":
            login()

        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()