"""
Objetivo:
    Criar uma função que exiba uma saudação personalizada.

Etapas:
    1. Receber um nome como parâmetro;
    2. Imprimir uma mensagem de boas-vindas com o nome informado.

Criado por: Bruna Loyola
Data: 02/05/2025
"""

#Declarando a função boas_vindas tendo um nome como parametro
def boas_vindas(nome):
    print(f"Seja bem-vindo(a), {nome}") #Imprimindo mensagem para o usuário

#Obtendo o nome com o usuário
nome_usuario = input("Digite seu nome: ")

#Chamando a função boas_vindas e passando o nome digitado pelo usuário como parametro
boas_vindas(nome_usuario)