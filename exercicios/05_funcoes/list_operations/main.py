"""
Objetivo:
    Criar funções para operações básicas com listas e importar em outro arquivo.

Etapas:
    1. Criar função soma_lista(lista);
    2. Criar função media_lista(lista);
    3. Criar função maior(lista);
    4. Importar e utilizar essas funções no programa principal.

Criado por: Bruna Loyola
Data: 02/05/2025
"""
#Importando funções do módulo list_operations
from list_operations import  soma_lista, media_lista, maior

#Declarando uma lista com números inteiros
lista = [5, 10, 15, 20]

#Chamando as funções dentro do print() e passando como parametro a lista declarada, imprimindo os resultados
print(f"A soma da lista: {soma_lista(lista)}")
print(f"A média da lista: {media_lista(lista)}")
print(f"O maior número da lista: {maior(lista)}")