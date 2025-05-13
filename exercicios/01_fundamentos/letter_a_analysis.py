"""
Objetivo:
    Analisar ocorrências da letra "a" em uma frase.

Etapas:
    1. Contar quantas vezes "a" aparece;
    2. Mostrar posição da primeira ocorrência;
    3. Mostrar posição da última ocorrência.

Criado por: Bruna Loyola  
Data: 02/05/2025
"""

#Pede ao usuário que digite uma frase e transforma todas as letras em minuscula
frase = input("Digite uma frase: ").lower()

#Conta quantas letras 'a', existem na frase
quantidade = frase.count('a')

#Insere em uma váriavel a posição em que apareceu a primeira letra 'a'
primeira_posicao = frase.find("a")

#Insere em uma váriavel a posição em que apareceu a ultima letra 'a'
ultima_posicao = frase.rfind("a")

#Informa ao usuário a quantidade de letras e a primeira e ultima posição em que aparecem
print("Essa é a quantidade de letras 'A': ", quantidade)
print(f"A primeira posição que o 'A' aparece é {primeira_posicao} e a ultima posição é {ultima_posicao}" )