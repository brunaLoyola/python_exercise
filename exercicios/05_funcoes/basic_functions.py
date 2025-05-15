"""
Objetivo:
    Praticar a criação de funções básicas com parâmetros e retorno.

Etapas:
    1. Criar função que recebe nome e idade e imprime uma frase personalizada;
    2. Criar função que recebe uma lista e imprime cada item.

Criado por: Bruna Loyola  
Data: 02/05/2025
"""

#Declarando uma lista com nomes de frutas
lista_global = ["Abacaxi", "Banana", "Uva", "Rocambole"]

#Declarando função imprime_frase com nome e idade passados por parâmetro
def imprime_frase(nome, idade):

    #Retorna uma mensagem personalizada com nome e idade do usuário 
    return print(f"Olá {nome}, você não parece ter {idade}")

#Declarando função listas que recebe lista como parâmetro
def lista(lista):

    #loop que passa por todos os itens da lista imprimindo eles
    for item in lista:
        print(item)

#Obtendo nome e idade do usuário
nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))

#Chamando função imprime_frase e passando por parâmetro o nome e idade recebidos do usuário
imprime_frase(nome_usuario, idade_usuario)

#Chamando função lista e passando a lista com as frutas por parâmetro
lista(lista_global)