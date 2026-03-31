def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    return digito2 == int(cpf[10])



def cadastro():
    print("Cadastro de usuário")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    cpf = str(input("Digite seu CPF: "))
    aux = False

    for letra in email:
        if letra == "@":
            aux = True
    
    if aux == False:
        print("\nEmail inválido!")
        return


  

    
    if validar_cpf(cpf) == False:
        print("CPF inválido!")
        return

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "r") as arquivo:
        if arquivo != False:
            for dado in arquivo:
                if dado.strip().split(",")[3] == cpf:
                    print("CPF já cadastrado!")
                    return
            
    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{senha},{cpf}\n")
        

    print(f"\nUsuário {nome} cadastrado com sucesso!")




def login():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    dados = []
    aux = False
    
    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "r") as arquivo:
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