"""
Objetivo:
    Receber informações do usuário, converter os tipos e exibir o tipo de cada variável.

Etapas:
    1. Solicitar nome, idade e altura do usuário;
    2. Exibir o tipo de cada variável e uma mensagem com as informações fornecidas.
"""

#Obtém informações do usuário e as convertem quando necessário em inteiro ou float
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura"))

#Imprime o tipo de cada informação obtida
print(type(nome)) #str
print(type(idade)) #int
print(type(altura)) #float

#Imprime os dados informados 
print(f"{nome} tem {idade} anos e mede {altura} metros")