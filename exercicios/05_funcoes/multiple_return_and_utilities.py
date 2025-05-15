"""
Objetivo:
    Utilizar retorno múltiplo em funções e aplicar utilidades com strings e parâmetros padrão.

Etapas:
    1. Criar função que retorna soma, subtração, multiplicação e divisão de dois números;
    2. Criar função que calcula área de retângulo com valores padrão;
    3. Criar função que conta quantas vogais há em uma palavra.

Criado por: Bruna Loyola  
Data: 02/05/2025
"""

#Declarando função aritmetica que recebe dois números por parametro
def aritmetica(numero01, numero02):
    #Retorna uma mensagem com os resultados da adição, subtração, multiplicação e divisão
    return f"Soma:{numero01+numero02} \n Subtração: {numero01-numero02} \n Multiplicação: {numero01 * numero02} \n Divisão: {numero01/numero02}"

#Declarando função calcular_area que recebe base e altura por parametro
def calcular_area(base, altura):

    #Condição para verificar se base e altura não são iguais 
    if base == altura:
        return print("Isso é um quadrado, não um retângulo")
    
    #Condição para verificar se o número não é negativo
    elif base <= 0 or altura <=0:
        return print("Não é possível calcular a área")
    
    #Condição em que imprime a resposta com o valor da área do retângulo
    else: 
        return print(f"O valor da área do retângulo é de {base*altura}")

#Declarando função calcular_vogais que recebe uma palavra por parametro
def calcular_vogais(palavra):
    #Conta a quantidade de vogais somando com a função .count()
    vogais = palavra.count('a') + palavra.count('e') + palavra.count('i') + palavra.count('o') + palavra.count('u')
    
    #Retorna para o usuário o total de vogais na palavra
    return print("Quantidade total de vogais: ", vogais)

#Obtendo dois números com o usuário
numero01_usuario = int(input("Digite o primeiro número: "))
numero02_usuario = int(input("Digite o segundo número: "))

#Imprimindo uma mensagem para o usuário enquanto chama a função aritmetica passando os dois números obtidos por parametro
print("Esses são os resultados das operações aritméticas\n", aritmetica(numero01_usuario, numero02_usuario))

#Obtendo base e altura com o usuário
base_usuario = int(input("Digite o valor da base:"))
altura_usuario = int(input("Digite o valor da altura:"))
#Chamando a função calcular_area, passando base e altura digitados como parametro
calcular_area(base_usuario, altura_usuario)

#Obtendo uma palavra com o usuário
palavra_usuario = list(input("Digite a palavra:").lower()) #transformando em lista e deixando em letras minusculas

#Chamando a função calcular_vogais passando a palavra informada pelo usuário como parametro
calcular_vogais(palavra_usuario)