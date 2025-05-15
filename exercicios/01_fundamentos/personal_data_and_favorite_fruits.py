"""
Objetivo:
    Armazenar e exibir dados pessoais e frutas favoritas.

Etapas:
    1. Criar variáveis com nome, idade e altura;
    2. Criar lista com 3 frutas favoritas;
    3. Criar dicionário com os dados pessoais;
    4. Exibir todas as informações organizadas.
"""

#Obtém as informações do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

#Declara uma lista vazia que será trabalhada
frutas_favoritas = []

#Solicita ao usuário atráves de um loop quais suas frutas favoritas 
for i in range(1, 4): #O loop acontecerá 3 vezes
    fruta = input(f"Digite a {i}° fruta favorita: ")
    frutas_favoritas.append(fruta) #Adiciona a fruta digitada na lista declarada anteriormente

#Insere em um dicionário as informações coletadas 
dados = {
    "nome": nome,
    "idade": idade,
    "altura": altura,
    "frutas_favoritas": frutas_favoritas
}

#Imprime as informações utilizando um loop, para acessar as informações do dicionario
for chave, valor in dados.items(): #Percorre cada posição do dicionário
    print(f"{chave.capitalize()} : {valor}")