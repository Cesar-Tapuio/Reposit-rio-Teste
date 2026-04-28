# # Criando um dicionário de um produto
# produto = {
#     "nome": "Notebook",
#     "preco": 2500.00,
#     "estoque": 10,
#     "disponivel": True
# }

#Lista de dict

# lista_usuarios = [
#     {"id": 1, "nome": "Alice"},
#     {"id": 2, "nome": "Bob"}
# ]


# # Acessando valores
# print(produto["nome"])  # Saída: Notebook

# # Modificando e adicionando elementos
# produto["estoque"] = 15
# produto["garantia"] = "1 ano"

# # Iterando sobre o dicionário
# for chave, valor in produto.items():
#     print(f"{chave}: {valor}")


lista_usuarios = []

def cadastro():

  nome = input("\nDigite o nome do usuario: ")
  new_user_id = len(lista_usuarios) + 1
  idade = int(input("Idade do usuario: "))
  senha = input("Nova senha: ")
  confirmar_senha = ""


  while confirmar_senha != senha:
    confirmar_senha = input ("Confirme sua senha: ")
    if confirmar_senha != senha:
      print("As senhas não coincidem, confirme sua seha novamente\n")
    else:
      print(f"\nCadastro realizado com sucesso\nID do usuario: {new_user_id}\n")

      novo_usuario = {
          "id": new_user_id,
          "nome": nome,
          "idade": idade,
          "senha": senha
      }
      lista_usuarios.append(novo_usuario)




def removerUsuario():
  usuario_removido = {
        "id": 0,
        "nome": "Usuario Removido",
        "idade": 0,
        "senha": ""
      }
  id = int(input("Digite o ID do usuario que deseja remover: "))
  
  for usuario in lista_usuarios:
    if usuario["id"] == id:
      lista_usuarios.remove(usuario)
      print(f"Usuario com ID {id} removido com sucesso")
      lista_usuarios.append(usuario_removido)
      lista_usuarios.sort(key=lambda x: x["id"]) #Organizar a lista em ordem crescente de id
      return

  print(f"\nUsuario com ID {id} não encontrado")






def listarUsuarios():
  for usuario in lista_usuarios:
    print(f"\nID: {usuario['id']}")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")






def menuFuncionario():

  opcao = 1

  while opcao != 0:
    print("\n1 - Cadastrar novo usuario")
    print("2 - Remover cadastro de usuario")
    print("3 - Listar usuarios cadastrados")
    print("0 - Voltar")

    opcao = int(input("Opção: "))

    if opcao == 1:
      cadastro()

    elif opcao == 2:
      removerUsuario()

    elif opcao == 3:
      listarUsuarios()






def loginUsuario():

  opcao = 1

  while opcao == 1:

    id = int(input("Digite o ID do usuario: "))
    senha = input("Digite a senha do usuario: ")

    for usuario in lista_usuarios:
      if usuario["id"] == id and usuario["senha"] == senha:
        print("Login realizado com sucesso")
        return
    print("\nLogin falhou")
    print("\n0 - Voltar")
    print("1 - Tentar novamente")

    opcao = int(input("Opção: "))

    if opcao == 0:
      return





def menuUsuario():
 
  opcao = 1

  while opcao != 0:

    print("\n1 - Login")
    print("0 - Voltar")

    opcao = int(input("Opção: "))

    if opcao == 1:
      loginUsuario()





def menuPrincipal():

  opcao = 1

  while opcao != 0:
    print("\n1 - Login usuario")
    print("2 - Login Funcionario")
    print("0 - Finalizar programa")

    opcao = int(input("Opção: "))

    if opcao == 1:
      menuUsuario()

    elif opcao == 2:
      menuFuncionario()

    elif opcao == 0:
      print("Programa finalizado")



menuPrincipal()
