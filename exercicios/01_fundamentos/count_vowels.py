"""
Objetivo:
    Criar uma função que conte quantas vogais existem em uma string.

Etapas:
    1. Receber uma string como parâmetro;
    2. Verificar e contar as vogais presentes;
    3. Retornar o total de vogais.
"""
#Peça um nome
nome = list(input("Digite seu nome:").lower())

#conta a quantidade de vogais somando com a função .count()
vogais = nome.count('a') + nome.count('e') + nome.count('i') + nome.count('o') + nome.count('u')

#Mostrando quantas vogais o nome possui
print(f"Seu nome possui {vogais} vogais")