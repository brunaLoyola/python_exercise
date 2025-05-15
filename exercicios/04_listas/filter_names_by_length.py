"""
Objetivo:
    Retornar nomes com mais de 5 letras em ordem alfabética.

Etapas:
    1. Receber uma lista de nomes;
    2. Filtrar os que possuem mais de 5 letras;
    3. Ordenar alfabeticamente;
    4. Retornar a nova lista.

Criado por: Bruna Loyola
Data: 02/05/2025
"""
#Declarando listas vazias que serão utilizadas
lista = []  #Lista com com todos os nomes
cinco_letras = [] #Lista para nomes que tem mais de cinco letras

#Condicional que irá ser verdadeiro enquanto o usuário não digitar sair
while True:
    nome = input("Digite um nome (digite 'sair' quando finalizar):")

    if nome == 'sair':
        break
    #Caso não tenha sido digitado sair, o nome digitado é adicionado a lista
    else:
        lista.append(nome)

#Loop para percorrer a lista de nomes e verificar qual possue mais de 5 letras
for item in lista:
    if len(item) > 5: 
        cinco_letras.append(item) #tendo mais que cinco letras, o nome é adicinado na lista

#Utilizando a função sort(), para colocar em ordem alfabética
cinco_letras.sort()
print("Os nomes que possuem mais de cinco letras são: \n", cinco_letras) #Imprimindo os nomes na tela
