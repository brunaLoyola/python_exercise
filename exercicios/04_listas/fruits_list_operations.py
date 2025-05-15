"""
Objetivo:
    Manipular uma lista de frutas com inserções e remoções.

Etapas:
    1. Criar uma lista com 5 frutas;
    2. Adicionar uma fruta nova;
    3. Remover a primeira fruta;
    4. Exibir a lista final.
"""

#Lista de frutas já com as frutas declaradas
frutas = ["uva", "pera", "maca", "banana", "amora"]

#Adicionando uma fruta na ultima posição da lista
frutas.append("framboesa")

#Exibindo a lista atualizada
print(frutas)

#Removendo o primeiro item da lista
frutas.pop(0)

#Exibindo a lista atualizada
print(frutas)