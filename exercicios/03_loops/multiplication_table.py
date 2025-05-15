"""
Objetivo:
    Exibir a tabuada de um número fornecido pelo usuário.

Etapas:
    1. Solicitar um número do usuário;
    2. Exibir a tabuada desse número de 1 a 10.
"""

#Obtém um número 
numero = int(input("Digite um numero: "))

#Imprime a tabuada do número obtido de 1 a 10, utilizando um loop.
for i in range(1, 11):
    print(f"{numero} x {i}: {numero*i}")