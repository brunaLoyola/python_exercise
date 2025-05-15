"""
Objetivo:
    Contar o número de palavras em uma frase recebida por uma função.

Etapas:
    1. Receber uma frase como parâmetro;
    2. Separar as palavras;
    3. Retornar a quantidade de palavras.
"""

def conta_palavras(frase):
    lista_palavras = frase.split()
    return len(lista_palavras)

frase_usuario = input("Digite uma frase: ")
print(conta_palavras(frase_usuario))