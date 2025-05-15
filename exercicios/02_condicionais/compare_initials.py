"""
Objetivo:
    Comparar iniciais de nomes ignorando maiúsculas, minúsculas e espaços.

Etapas:
    1. Receber dois nomes;
    2. Verificar se começam com a mesma letra.
"""

#Obtém dois nomes e transforma em letras minusculas
primeiro_nome = input("Digite o primeiro nome: ").lower()
segundo_nome = input("Digite o segundo nome: ").lower()

#Atráves de condicionais verifica se a primeira letra dos dois números são iguais, utilizando o índice 0
if primeiro_nome[0] == segundo_nome[0]:
    print(f"As duas letras são iguais, sendo {primeiro_nome[0]}!")
else:
    print(f"As letras são diferentes sendo a do primeiro nome '{primeiro_nome[0]}' e do segundo nome '{segundo_nome[0]}'")