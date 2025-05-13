"""
Objetivo:
    Criar uma lista de compras e permitir adicionar itens até digitar 'sair'.

Etapas:
    1. Solicitar ao usuário que adicione itens a uma lista;
    2. Exibir a lista completa ao final e informar quantos itens ela contém.

Criado por: Bruna Loyola
Data: 29/04/2025
"""

#Declara uma váriavel do tipo lista vazia
lista_compras = []

#O while inicia em 'True' para poder entrar no bloco de códigos
while True:
    item = input("Digite o item para adicionar a lista (ao finalizar digite 'sair'): ")

    #Atráves de uma condicional, caso o usuário digite sair, o bloco de códigos é finalizado com um 'break'
    if item == 'sair':
        break
    else:
        lista_compras.append(item) #Caso não seja digitado 'sair', um item é adicionado na lista de compras

#Imprime a lista de compras completa
print(lista_compras)