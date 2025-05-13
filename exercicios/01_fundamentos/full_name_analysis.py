"""
Objetivo:
    Trabalhar com manipulação e análise de nomes.

Etapas:
    1. Mostrar nome em maiúsculas e minúsculas;
    2. Contar letras desconsiderando espaços;
    3. Mostrar primeiro nome e quantas letras ele tem.

Criado por: Bruna Loyola  
Data: 02/05/2025
"""

#Pede o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

#Transforma em letra maiuscula atráves da função .upper()
maiuscula = nome_completo.upper()

#Transforma em letra minuscula atráves da função .lower()
minuscula = nome_completo.lower()

#Imprime o resultado do nome com as letras modificadas para todas maiusculas e depois minusculas
print(f"Esse é seu nome com letra maiúscula: {maiuscula}")
print(f"Esse é seu nome com letra minúscula: {minuscula}")

#Retira os espaços da váriavel que foi tratada para serem minusculas as letras digitadas pelo usuário com replace 
nome_sem_espaco = len(minuscula.replace(" ", "")) #conta quantas letras tem com o len()

#Mostra ao usuário a quantidade de letras que tem o nome (sem contar com os espaços digitados)
print("Quantidade de letras no seu nome completo: ", nome_sem_espaco)

#Transformando o nome que o usuário informou em lista (exemplo: ['maria', 'clara'])
nome_lista = nome_completo.split()

#Informa ao usuário seu primeiro nome e a quantidade de letras que tem seu primeiro nome
print(f"Seu primeiro nome é {nome_lista[0]} e seu nome tem {len(nome_lista[0])}")