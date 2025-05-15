"""
Objetivo:
    Verificar se um número é par ou ímpar.

Etapas:
    1. Receber um número como parâmetro;
    2. Verificar se o número é divisível por 2;
    3. Retornar se é par ou ímpar.

Criado por: Bruna Loyola
Data: 02/05/2025
"""

#Declarando a função par_impar que recebe um número como parametro
def par_impar(numero):

    #Condição que verifica se o número é negativo
    if numero < 0:
        return print("O número é negativo")  
    
    #Condição que verifica se o número é par atráves do resto da divisão
    elif numero % 2 == 0:
        return print("O número é par") 
    
    #Condição que verifica se o número é impar
    else:
        return print("O número é ímpar") 


#Obtendo o número com o usuário
numero_usuario = int(input("Digite um número: "))

#Chamando a função e passando o número digitado pelo usuário como parâmetro
par_impar(numero_usuario)