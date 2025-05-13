"""
Objetivo:
    Verificar se um número está dentro de um intervalo e validar usuários.

Etapas:
    1. Verificar se um número fornecido pelo usuário está entre 10 e 20;
    2. Validar se o usuário é "admin" ou "root".

Criado por: Bruna Loyola
Data: 28/04/2025
"""

#Obtém um número com o usuário e o converte para inteiro
numero = int(input("Digite um número"))

#Utiliza de condições para verificar se um número está entre 10 e 20
if numero >=10 and numero<=20:
    print(f"O número {numero} está entre 10 e 20")
else:
    print(f"O número {numero} não está entre 10 e 20")

#Verifique se o nome do usuário é "admin" ou "root"

#Testando usuário "admin"

usuario = "admin"

if usuario == "admin":
    print("O usuário é um administrador")
else:
    print("O usuário não é um administrador")

#Testando usuário root
usuario_02 = "root"

if usuario_02 == "admin":
    print("O usuário é um administrador")
else:
    print("O usuário não é um administrador")