import hashlib
import re

ARQUIVO = "usuarios.txt"




def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def parse_usuario(linha):
    nome, email, senha, cpf = linha.strip().split(",")
    return {"nome": nome, "email": email, "senha": senha, "cpf": cpf}


def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as f:
            return [parse_usuario(linha) for linha in f]
    except FileNotFoundError:
        return []


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        for u in usuarios:
            f.write(f"{u['nome']},{u['email']},{u['senha']},{u['cpf']}\n")



def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    return digito2 == int(cpf[10])



def cadastro():
    print("\nCadastro de usuário")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = hash_senha(input("Senha: "))
    cpf = input("CPF: ")

    if not validar_email(email):
        print("Email inválido!")
        return

    if not validar_cpf(cpf):
        print("CPF inválido!")
        return

    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["cpf"] == cpf:
            print("CPF já cadastrado!")
            return

    usuarios.append({
        "nome": nome,
        "email": email,
        "senha": senha,
        "cpf": cpf
    })

    salvar_usuarios(usuarios)
    print("Usuário cadastrado!")


def login():
    nome = input("\nNome: ")
    senha = hash_senha(input("Senha: "))

    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print("Login realizado!")
            return True

    print("Login inválido!")
    return False


def excluir_usuario():
    cpf = input("\nCPF: ")
    senha = hash_senha(input("Senha: "))

    usuarios = carregar_usuarios()
    novos = []

    encontrado = False

    for u in usuarios:
        if u["cpf"] == cpf and u["senha"] == senha:
            encontrado = True
        else:
            novos.append(u)

    if encontrado:
        salvar_usuarios(novos)
        print("Usuário excluído!")
    else:
        print("Dados incorretos!")



def alterar_nome():
    cpf = input("CPF: ")
    novo_nome = input("Novo nome: ")

    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["cpf"] == cpf:
            u["nome"] = novo_nome
            salvar_usuarios(usuarios)
            print("Nome atualizado!")
            return

    print("Usuário não encontrado!")


def alterar_email():
    cpf = input("CPF: ")
    novo_email = input("Novo email: ")

    if not validar_email(novo_email):
        print("Email inválido!")
        return

    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["cpf"] == cpf:
            u["email"] = novo_email
            salvar_usuarios(usuarios)
            print("Email atualizado!")
            return

    print("Usuário não encontrado!")


def alterar_senha():
    cpf = input("CPF: ")
    nova_senha = hash_senha(input("Nova senha: "))

    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["cpf"] == cpf:
            u["senha"] = nova_senha
            salvar_usuarios(usuarios)
            print("Senha atualizada!")
            return

    print("Usuário não encontrado!")



def menu_cliente():
    while True:
        print("\n1 - Cadastrar")
        print("2 - Login")
        print("3 - Voltar")

        op = input("Opção: ")

        if op == "1":
            cadastro()
        elif op == "2":
            login()
        elif op == "3":
            break
        else:
            print("Inválido")


def menu_funcionario():
    while True:
        print("\n1 - Excluir")
        print("2 - Alterar")
        print("3 - Voltar")

        op = input("Opção: ")

        if op == "1":
            excluir_usuario()

        elif op == "2":
            print("\n1 - Nome")
            print("2 - Email")
            print("3 - Senha")

            sub = input("Opção: ")

            if sub == "1":
                alterar_nome()
            elif sub == "2":
                alterar_email()
            elif sub == "3":
                alterar_senha()

        elif op == "3":
            break


def menu_principal():
    while True:
        print("\n1 - Cliente")
        print("2 - Funcionário")
        print("3 - Sair")

        op = input("Opção: ")

        if op == "1":
            menu_cliente()
        elif op == "2":
            menu_funcionario()
        elif op == "3":
            break


menu_principal()