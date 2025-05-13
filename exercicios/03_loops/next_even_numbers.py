"""
Objetivo:
    Gerar os 10 primeiros números pares maiores que um número informado pelo usuário.

Etapas:
    1. Solicitar um número inteiro ao usuário;
    2. Calcular os próximos 10 números pares após esse valor;
    3. Exibir os números gerados.

Criado por: Bruna Loyola
Data: 04/05/2025
"""

#Obtém um núemero e converte para inteiro
numero_usuario = int(input("Digite um número inteiro: "))
numeros_gerados = []

#Ajusta o número para o próximo par maior
if numero_usuario % 2 != 0:
    numero_usuario += 3
else: 
    numero_usuario += 2

#Loop que gera e imprime os 10 próximos números pares usando range
for n in range(numero_usuario, numero_usuario+20, +2):
    print(n)


