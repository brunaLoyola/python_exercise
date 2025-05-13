"""
Objetivo:
    Trabalhar com listas e compreensão de listas para filtragem e soma.

Etapas:
    1. Criar lista com números de 1 a 5;
    2. Criar nova lista com os quadrados dos números;
    3. Criar lista apenas com os números pares;
    4. Somar os números pares.

Criado por: Bruna Loyola
Data: 30/04/2025
"""


numeros = [1, 2, 3, 4, 5]

#Lista com os valores ao quadrado
quadrado = [num * num for num in numeros]
print(quadrado)

#Lista com os pares
pares = [num for num in numeros if num % 2 == 0]
print(pares)

#Soma dos pares
print(sum(pares))