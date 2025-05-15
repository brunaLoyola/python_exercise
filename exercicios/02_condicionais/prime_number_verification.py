"""
Objetivo:
    Verificar se um número é primo.

Etapas:
    1. Solicitar um número inteiro ao usuário;
    2. Verificar se o número é primo ou não.
"""

#Obtém um número e converte para inteiro
numero = int(input("Digite um número válido: "))

#Atráves de condições verifica se o número é primo
if numero >= 2:
    confirma = True #Assume inicialmente que o número é primo
    for i in range(2, int(numero**0.5) + 1): #Testa divisores de 2 até a raiz quadrada de 'numero'
        if numero % i == 0:
            confirma = False # Encontrou um divisor, não é primo
            break
    if confirma: # confirma = True
        print("É primo")
    else:
        print("Não é primo")
else:
    print("Número inválido") #Números menores que dois não são considerados primos