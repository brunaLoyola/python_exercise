"""
Objetivo:
    Cadastrar informações de três usuários e determinar quem é maior de idade.

Etapas:
    1. Solicitar nome e idade de três usuários;
    2. Exibir todos os usuários cadastrados;
    3. Verificar quem é maior ou menor de idade.
"""

#Cadastre nome e idade de 3 pessoas usando listas aninhadas.
informacoes_usuario = []

for quantidade in range(3):
    print(f"Usuário {quantidade+1}")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    informacoes_usuario.append([nome, idade])

#Ao final, mostre:
#Todas as pessoas cadastradas
for pessoa in informacoes_usuario:
    print(f"Nome:{pessoa[0]}")
    print(f"Idade:{pessoa[1]}")

#Quem é maior de idade
for pessoa in informacoes_usuario:
    if int(pessoa[1]) >= 18:
        print(f"{pessoa[0]} é maior de idade")
    #Quem é menor de idade
    else:
        print(f"{pessoa[0]} é menor de idade")