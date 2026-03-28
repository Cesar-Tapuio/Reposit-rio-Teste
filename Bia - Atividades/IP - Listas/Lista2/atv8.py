# O laboratório de computação do INF/UFG realiza um inventário semestral de equipamentos.
# Utilizando o laço for, crie um programa que leia o nome e o valor (em reais) de N equipamentos
# cadastrados, e ao final exiba:
# • a lista de todos os equipamentos com seus valores;
# • o valor total do inventário;
# • o nome e o valor do equipamento mais caro;
# • o nome e o valor do equipamento mais barato.
# Entrada: número N de equipamentos; nome e valor de cada equipamento.
# Saída: lista dos equipamentos, valor total do inventário, equipamento mais caro e mais barato.


listaEquip = []
nEquip = int(input("Numero de equipamentos: "))

for i in range(nEquip):
    nomeEquip = input("Nome do equipamento: ")
    precoEquip = float(input("Preço do equipamento: "))

    novoEquip = {
        "nome": nomeEquip,
        "preco": precoEquip
    }
    listaEquip.append(novoEquip)

listaEquip.sort(key=lambda x: x["preco"]) # Ordena pelo preço

for equipamento in listaEquip:
    print(f"Equipamento: {equipamento['nome']} - Preço: R$ {equipamento['preco']}")

maisCaro = listaEquip[-1]
maisBarato = listaEquip[0]

print(f"\nEquipamento mais caro: {maisCaro['nome']} - R$ {maisCaro['preco']}")
print(f"Equipamento mais barato: {maisBarato['nome']} - R$ {maisBarato['preco']}")





   
