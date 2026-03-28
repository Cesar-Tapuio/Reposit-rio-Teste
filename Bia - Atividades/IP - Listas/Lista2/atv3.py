# O sistema de autenticação de um laboratório do CEIA/UFG deve solicitar uma senha ao usuário.
# Utilizando o laço while, crie um programa que permita ao usuário tentar digitar a senha correta até
# 3 vezes. A senha correta é bia2025. O programa deve exibir:
# • "Acesso liberado!" se a senha estiver correta;
# • "Senha incorreta. Tentativa X de 3." a cada erro;
# • "Acesso bloqueado. Entre em contato com o suporte." após 3 erros.
# Entrada: senha digitada pelo usuário (até 3 tentativas).
# Saída: mensagem de acesso liberado ou bloqueado após esgotar tentativas.


tentativa = 0

while  tentativa < 3:
    tentativa += 1
    senha = input("Digite sua senha: ")
    
    if senha == "bia2025":
        break
    else:
        print("\nSenha incorreta!\nTente novamente\n")

if senha == "bia2025":
    print("\nAcesso liberado!")

else:
    print("\nAcesso bloqueado após esgotar tentativas!")
