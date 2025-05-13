"""
Objetivo:
    Demonstrar o uso de loops em Python com contagem e validação de senha.

Etapas:
    1. Criar um contador que imprima números de 1 até 5;
    2. Criar um loop que permita a entrada de senha até que a senha correta seja informada.

Criado por: Bruna Loyola
Data: 28/04/2025
"""

#Inicializando o contador com 1
contador = 1

#Loop que imprime de 01 a 05
while contador <=5:
    print(contador)
    contador+=1 

#Loop que começa como 'True' para entrar.
while True:
    senha = int(input("Digite uma senha: "))
    
    #Condição que verifica a senha informada pelo usuário, se for a correta ele finaliza o loop
    if senha == 1234:
        print("Senha correta")
        break
    else:
        print("Senha incorreta")