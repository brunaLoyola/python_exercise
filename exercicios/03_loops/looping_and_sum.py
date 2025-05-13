"""
Objetivo:
    Utilizar laços de repetição para imprimir números e calcular a soma de um intervalo.

Etapas:
    1. Imprimir números de 1 a 10;
    2. Imprimir números pares de 0 a 20;
    3. Calcular a soma de 1 a 100 e exibir o resultado.

Criado por: Bruna Loyola
Data: 29/04/2025
"""

#Imprime os números de 1 a 10
for x in  range(1, 11):
    print(x)

#Imprime todos os números pares de 0 a 20
for par in  range(0, 21, 2):
    print(par)

#Soma os números de 1 a 100
resultado = 0
for num in  range(0, 100+1):
    resultado += num
    print(resultado)