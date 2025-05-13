"""
Objetivo:
    Solicitar dados pessoais e calcular o ano de nascimento com base na idade.

Etapas:
    1. Solicitar nome, idade e peso do usuário;
    2. Calcular o ano de nascimento;
    3. Exibir os dados organizadamente.

Criado por: Bruna Loyola
Data: 02/05/2025
"""

#Importa o módulo datetime para acessar a data atual
from datetime import datetime

#Obtém o ano atual
ano_atual = datetime.now().year

#Obtem as informações do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

#Faz o cálculo subtraindo o ano atual com a idade do usuário
ano_nascimento = ano_atual - idade

#Imprime as informações do usuário e seu ano de nascimento
print(f"Seu nome é {nome}, você tem {idade} anos e nasceu no ano de {ano_nascimento}, seu peso é {peso}kg")