"""
Objetivo:
    Verificar se um número é positivo, negativo ou zero.

Etapas:
    1. Solicitar um número ao usuário;
    2. Verificar sua condição (positivo, negativo ou zero);
    3. Exibir o resultado.

Criado por: Bruna Loyola
Data: 01/05/2025
"""
#Obtem o número e o converte para inteiro
numero = int(input("Digite um numero: "))

#Utiliza de condições para informar ao usuário o que é o número
if numero == 0:
    print("Seu número é 0") 
elif numero < 0:
    print("Seu número é negativo")
else:
    print("Seu número é positivo")