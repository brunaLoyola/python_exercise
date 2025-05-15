"""
Objetivo:
    Comparar dois números fornecidos pelo usuário e exibir informações sobre sua relação.

Etapas:
    1. Receber dois números do usuário;
    2. Determinar qual número é maior, se são iguais ou se o primeiro é menor ou maior que o segundo.
"""

#Obtem dois números e os convertem para inteiro
numero_01 = int(input("Digite o primeiro número: "))
numero_02 = int(input("Digite o segundo número: "))

#Atráves de condições verifica qual é o maior número entre eles
if numero_01 > numero_02:
    print("O maior número é:", numero_01)
else:
    print("O maior número é:", numero_02)

#Atráves de condições verifica se os números são iguais
if numero_01 == numero_02:
    print("Os dois números são iguais !")
else:
    print("Os números são diferentes")

#Atráves de condições verificam se o primeiro é menor que o segundo número
if numero_01 < numero_02:
    print("O primeiro número é menor que o segundo número")
elif numero_01 == numero_02: #Se eles são iguais
    print("O primeiro e o segundo número são iguais")
else: #Ou se o primeiro número é maior que o segundo
    print("O primeiro número é maior que o segundo número")