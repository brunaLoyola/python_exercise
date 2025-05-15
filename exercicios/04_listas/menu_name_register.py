"""
Objetivo:
    Criar um menu interativo que permita cadastrar e listar nomes.

Etapas:
    1. Exibir menu com 3 opções: Cadastrar nome, Listar nomes cadastrados e Sair;
    2. Utilizar laço de repetição while e input para navegação;
    3. Armazenar nomes em uma lista e exibir quando solicitado;
    4. Encerrar o programa ao selecionar a opção de sair.

Criado por: Bruna Loyola
Data: 02/05/2025
"""

#Declarando uma lista vazia que será utilizada
lista_nomes = []

#Loop que será verdadeiro enquanto o usuário não digitar 03 (opção para sair)
while True:
    #Obtendo opção que o usuário deseja
    opcao = int(input("Digite uma das opções:\n 01 - Cadastrar nome \n 02 - Listar nomes cadastrados \n 03 - Sair\n"))

    #Condição em que se a opção for 01, irá adicionar um novo nome na lista_nomes
    if opcao == 1:
        nome = input("Digite um nome: ")
        lista_nomes.append(nome) #Adicionando nome a lista
        continue #Voltando ao inicio do loop

    #Condição em que caso seja a opção 02, irá listar os nomes de lista_nomes
    elif opcao == 2:
        for item in lista_nomes: #loop que passa por cada item
            print(item)
        continue #Voltando ao inicio do loop
    #Caso a condição seja a opção 03, o código é finalizado
    elif opcao == 3:
        break
    #Caso o usuário não digite uma opção válida ele imprime a imagem e volta para o inicio do loop
    else: 
        print("Opção incorreta")
        continue