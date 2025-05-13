"""
Objetivo:
    Validar o acesso de um usuário com base na idade e exibir informações do cadastro.

Etapas:
    1. Solicitar nome, idade e email do usuário;
    2. Negar o acesso se a idade for menor que 18 anos;
    3. Exibir um resumo do cadastro se a idade for 18 ou maior.

Criado por: Bruna Loyola
Data: 28/04/2025
"""

#Obtém as informações com o usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

#Utiliza de condições para verificar acesso do usuário
if idade < 18 and idade >=0: #Idades entre 0 e 17 anos
    print("Acesso negado")
#Caso seja maior de 18 anos, o usuário tem suas informações impressas
elif idade >= 18:
    print(f" Nome:{nome}\n Idade:{idade}\n Email:{email}.")
else: #Caso a idade informada seja inválida
    print("Idade inválida")


