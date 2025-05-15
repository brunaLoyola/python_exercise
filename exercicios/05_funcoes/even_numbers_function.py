"""
Exercício: Função para retornar números pares de uma lista
Descrição:
1. Crie uma função que receba uma lista de números e retorne apenas os números pares.
2. Crie outra função para pedir números ao usuário e adicionar à lista até que ele digite 'sair'.

Autor: Bruna Leandra Pontes Loyola
Data: 30/04/2025
"""

#Declarando a função numeros pares que recebe uma lista como parâmetro
def numeros_pares(lista_numeros):
    #Declarando lista de pares vazia
    lista_pares = []

    #Loop que passa por todos os números da lista recebidos atráves do parametro
    for i in lista_numeros:

        #condição para verificar se o número é par atráves do resto da divisão
        if i % 2 == 0:
            lista_pares.append(i) #Caso a condição seja verdadeira, o número é adicionado na lista de pares
    return lista_pares #Retorna a lista com os números pares

#Declarando função pedindo_numero
def pedindo_numero():

    #Declarando lista de usuários vazia
    lista_usuario = []

    #Loop que é verdadeiro enquanto o usuário não digitar 'sair'
    while True:
        numero = input("Digite um número para adicionar a lista (digite 'sair quando finalizar')")
        
        #Condição para verificar se o usuário não digitou sair
        if numero == 'sair':
            break #finaliza o loop
        else:
            lista_usuario.append(int(numero)) #Sendo digitado um número, é utilizado a conversão para número inteiro e adicionado a lista
    return lista_usuario

#Chamando as funções e colocando os resultados em variáveiss
lista_usuario = pedindo_numero()
lista_pares = numeros_pares(lista_usuario)

#Imprimindo lista de números pares
print("Lista de números pares: ", lista_pares)