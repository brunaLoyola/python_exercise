"""
Objetivo:
    Trabalhar com listas paralelas (nomes e idades) e filtragem condicional.

Etapas:
    1. Criar função que recebe duas listas: nomes e idades;
    2. Retornar apenas os nomes com idade maior que 18.

Criado por: Bruna Loyola  
Data: 02/05/2025
"""

#Declarando listas vazias que serão utilizadas
lista_nomes = []
lista_idades = []
maior_idade = []

#Declarando função nomes_idades recebendo como parametro nome e idade
def nomes_idades(nomes, idades):
    #loop que passa pela lista de idades
    for i in range(len(idades)):
        if idades[i] > 18: #condição para verificar se a idade na posição que o loop está é maior que 18
            maior_idade.append(nomes[i]) #Sendo maior o nome é adicionado na lista de maior de idade
    return print(maior_idade) #Retorna os nomes que são maiores de 18 anos

#loop que é verdadeiro enquanto o usuário não digitar sair
while True:
    nome_usuario = input("Digite seu nome (ou 'sair'):")

    #Condição em que verifica se o usuário digitou sair 
    if nome_usuario.lower() == 'sair':
        break #finaliza o loop
    else: #Se foi digitado um nome, é obtido a idade do usuário e adicionado nas listas
        idade_usuario = int(input("Digite sua idade: "))
        lista_nomes.append(nome_usuario)
        lista_idades.append(idade_usuario)
    
#Chamando função e passando lista de nomes e idades como parâmetro
nomes_idades( lista_nomes, lista_idades)