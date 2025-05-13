"""
Objetivo:
    Criar um programa que verifica a idade e autorização de um usuário para determinar o acesso.

Etapas:
    1. Perguntar a idade da pessoa (número inteiro);
    2. Perguntar se ela possui autorização ('S' para sim ou 'N' para não);
    3. Permitir a entrada apenas se a idade for maior que 18 ou se tiver autorização.

Criado por: Bruna Loyola
Data: 01/05/2025
"""

#Pergunta a idade do usuário, sendo convertida para número inteiro
idade = int(input("Digite sua idade (número inteiro): "))

#Perhunta se o usuário tem autorização e transforma em letra minúscula
autorizacao = input("Tem autorização (S ou N): ").lower()

#Condição para verificar se o usuário é maior de idade ou se tem autorização
if idade >= 18 or autorizacao == 's':
    print("Pode entrar!") #Caso uma das afirmações seja verdadeira, usuário pode entrar
elif idade < 18 or idade > 0 or autorizacao == 'n': 
    print("Acesso negado") #Se as duas informações forem falsas, então usuário não pode entrar