"""
Objetivo:
    Praticar funções de verificação e manipulação de strings.

Etapas:
    1. Criar função que verifica se nome começa com a letra "A";
    2. Criar função que inverte uma string.

Criado por: Bruna Loyola  
Data: 04/05/2025
"""
def verfica_primeira_letra(nome):
    if nome[0] == 'a':
        return "Esse nome começa com a letra 'a'"
    else:
        return "Esse nome não começa com a letra 'a'"

def inverte_string(palavra):
    palavra_invertida = list(palavra)
    palavra_invertida.reverse()
    return "".join(palavra_invertida)

nome_usuario = input("Digite um nome: ").lower()
palavra_usuario = input("Digite uma palavra: ")

print(verfica_primeira_letra(nome_usuario))
print(inverte_string(palavra_usuario))