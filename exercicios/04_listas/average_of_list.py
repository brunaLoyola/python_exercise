"""
Objetivo:
    Calcular a média dos valores de uma lista.

Etapas:
    1. Receber uma lista de números;
    2. Somar os valores;
    3. Dividir pela quantidade de elementos;
    4. Retornar a média.

Criado por: Bruna Loyola
Data: 04/05/2025
"""

lista_numeros = []

while True:
    numero = int(input("Digite um número inteiro para soma (digite '0', para finalizar): "))

    if numero == 0:
        break
    
    lista_numeros.append(numero)

soma_lista = sum(lista_numeros)
media = soma_lista / len(lista_numeros)

print("Essa é a soma da lista: ", soma_lista)
print("Essa é a média da lista: ", media)
