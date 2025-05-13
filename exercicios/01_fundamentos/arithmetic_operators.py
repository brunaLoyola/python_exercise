"""
Objetivo:
    Receber dois números do usuário e calcular os resultados dos operadores aritméticos básicos.

Etapas:
    1. Receber dois números inteiros do usuário;
    2. Exibir os resultados de soma, subtração, multiplicação, divisão, potência e resto da divisão.

Criado por: Bruna Loyola
Data: 27/04/2025
"""

#Usuario insere dois números inteiros
numero_01 = int(input("Digite o primeiro número: "))
numero_02 = int(input("Digite o segundo número: "))

#Imprime as operações aritméticas feitas com os números inseridos
print(f'A soma é: { numero_01 + numero_02}')
print(f'A subtração é: { numero_01 - numero_02}')
print(f'A multiplicação é: { numero_01 * numero_02}')
print(f'A divisão comum é: { numero_01 // numero_02}')
print(f'A pôtencia é: { numero_01 ** numero_02}')
print(f'O resto da divisão é: { numero_01 % numero_02}')