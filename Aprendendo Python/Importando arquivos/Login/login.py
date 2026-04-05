#Menu de funcionario que permite remover, listar e alterar usuarios



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
    print("\nCadastro de usuário")
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
        print("\nCPF inválido!")
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


def excluirUsuario():
    
    CPF = input("\nCPF do usuario: ")
    senha = input("Senha do usuario: ")
    verifUsuario = False

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "r") as arquivo:
        if arquivo != False:
            for usuario in arquivo:
                if usuario.strip().split(",")[3] == CPF:
                    if usuario.strip().split(",")[2] == senha:
                        verifUsuario = True
                        break

            if verifUsuario == True:
                with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "r") as arquivo:
                    linhas = arquivo.readlines()

                with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "w") as arquivo:
                    for linha in linhas:
                        if linha.strip().split(",")[3] != CPF:
                            arquivo.write(linha)

                print("\nUsuário excluído com sucesso!")
            else:
                print("\nUsuário ou senha incorretos!")


def alterarNome():
    CPF = input("\nDigite o CPF do usuário: ")
    senha = input("Digite a senha do usuário: ")
    novo_nome = input("Digite o novo nome: ")
    encontrado = False

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "w") as arquivo:
        for linha in linhas:
            dados = linha.strip().split(",")

            if dados[3] == CPF and dados[2] == senha:
                dados[0] = novo_nome
                encontrado = True

            arquivo.write(",".join(dados) + "\n")

    if encontrado:
        print("\nNome alterado com sucesso!")
    else:
        print("\nCPF ou senha incorretos!")


def alterarEmail():
    CPF = input("\nDigite o CPF do usuário: ")
    senha = input("Digite a senha do usuário: ")
    novo_email = input("Digite o novo email: ")
    encontrado = False
    valido = False

    for letra in novo_email:
        if letra == "@":
            valido = True

    if valido == False:
        print("\nEmail inválido!")
        return

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "w") as arquivo:
        for linha in linhas:
            dados = linha.strip().split(",")

            if dados[3] == CPF and dados[2] == senha:
                dados[1] = novo_email
                encontrado = True

            arquivo.write(",".join(dados) + "\n")

    if encontrado:
        print("\nEmail alterado com sucesso!")
    else:
        print("\nCPF ou senha incorretos!")


def alterarSenha():
    CPF = input("\nDigite o CPF do usuário: ")
    senha_atual = input("Digite a senha atual: ")
    nova_senha = input("Digite a nova senha: ")
    encontrado = False

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("/home/cesar/Documents/Python - Testes/Aprendendo/Aprendendo Python/Importando arquivos/Login/usuarios.txt", "w") as arquivo:
        for linha in linhas:
            dados = linha.strip().split(",")

            if dados[3] == CPF and dados[2] == senha_atual:
                dados[2] = nova_senha
                encontrado = True

            arquivo.write(",".join(dados) + "\n")

    if encontrado:
        print("\nSenha alterada com sucesso!")
    else:
        print("\nCPF ou senha incorretos!")


def login():
    nome = input("\nDigite seu nome de usuário: ")
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
                

def menuCliente():
    while True:
        
        print("\n1 - Cadastrar")
        print("2 - Login")
        print("3 - Voltar")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastro()
        elif escolha == "2":
            login()

        elif escolha == "3":
            print("Voltando...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menuFuncionario():
    
    while True:

        print("\n1 - Excluir usuário")
        print("2 - Alterar dados de usuário")
        print("3 - Sair")

        opcao = int(input())
        
        if opcao == 1:
            excluirUsuario()

        elif opcao == 2:
            while True:
                print("\n1 - Alterar nome")
                print("2 - Alterar email")
                print("3 - Alterar senha")
                print("4 - Voltar")
                alteracao = int(input())

                if alteracao == 1:
                    alterarNome()

                elif alteracao == 2:
                    alterarEmail()

                elif alteracao == 3:
                    alterarSenha()
                
                elif alteracao == 4:
                    break

                else:
                    print("Opção inválida!")

        elif opcao == 3:
            break

        else:
            print("Opção inválida")


def menuPrincipal():

    while True:

        opcao = int(input("\n1 - Cliente\n2 - Funcionario\n3 - Sair\n--> "))

        if opcao == 1:
            menuCliente()
            
        elif opcao == 2:
            menuFuncionario()
            
        elif opcao == 3:
            break
        else:
            print("\nOpção inválida!\n")



menuPrincipal()