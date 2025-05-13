"""
Objetivo:
    Manipular uma lista de nomes realizando alterações e verificações.

Etapas:
    1. Criar lista com 5 nomes;
    2. Exibir o primeiro e o último nome;
    3. Alterar o segundo nome;
    4. Adicionar novo nome ao final;
    5. Remover o terceiro nome;
    6. Verificar o tamanho da lista;
    7. Verificar se um nome está presente.

Criado por: Bruna Loyola
Data: 01/05/2025
"""


lista_nomes = ["Bruna", "Jean", "Helena", "Maria", "Antonio"]

#Mostrando o primeiro nome e o último nome da lista
print(f"O primeiro nome da lista é {lista_nomes[0]}, e o último nome da lista é {lista_nomes[-1]}")

#Alterando o segundo nome (posição 1, pois listas iniciam em 0)
lista_nomes[1] = "Cesar"
print(lista_nomes)

#Adicionando um novo nome ao final da lista
lista_nomes.append("Fernanda")
print(lista_nomes)

#Removendo o terceiro nome (posição das listas iniciam em 0, logo o terceiro nome está na posição 02)
lista_nomes.pop(2)
print(lista_nomes)

#Mostrando o tamanho da lista
print(len(lista_nomes))

#Verificando se um nome está na lista
print("Jean" in lista_nomes)