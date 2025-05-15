"""
Objetivo:
    Criar um programa de compras que armazena produtos e calcula o total.

Etapas:
    1. Perguntar quantos produtos a pessoa deseja comprar;
    2. Receber o nome e o preço de cada produto;
    3. Exibir a lista de produtos cadastrados;
    4. Calcular e mostrar o total gasto;
    5. Informar qual foi o produto mais caro.
"""

produtos = int(input("Quantos produtos você deseja comprar: "))
lista_informacao = []

for produto in range(1, produtos+1):
    nome = input(f"Digite o nome do {produto}° produto: ")
    valor = float(input(f"Digite o valor do {produto}° produto:"))
    lista_informacao.append([nome, valor])
print(lista_informacao)