"""
Objetivo:
    Trabalhar com manipulação de strings e listas.

Etapas:
    1. Pedir frase ao usuário;
    2. Inverter a frase;
    3. Separar palavras com split();
    4. Juntar com hífen.
"""

#Obtém uma frase com o usuário e separa as palavras usando .split()
frase_usuario = input("Digite uma frase: ").split()
frase_reverse = frase_usuario[::-1] #Inverte a lista de palavras
frase_com_hifen = "-".join(frase_reverse)  #Junta as palavras invertidas com hífen

#Imprime a frase invertida e com hífen
print("A frase invertida fica: ", frase_com_hifen)


