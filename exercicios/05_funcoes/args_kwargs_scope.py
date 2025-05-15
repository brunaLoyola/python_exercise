"""
Objetivo:
    Trabalhar com parâmetros variados, *args, **kwargs, escopo de variáveis locais e globais.

Etapas:
    1. Criar função que calcula a média de vários números com *args;
    2. Criar função relatorio(**dados) que imprime os dados;
    3. Criar variável global total e função que soma um número a ela;
    4. Criar função com variável local e tentar acessá-la fora da função.

Criado por: Bruna Loyola  
Data: 02/05/2025
"""

#Declarando váriavel global que inicia em 
global_total = 0 

#Declarando função calcular_media que recebe um *args como parâmetro
def calcular_media(*args):

    #Calcula a média somando os itens recebidos e dividindo pela quantidade de números
    media = sum(args) / len(args)

    #Retorna uma mensagem com a média
    return print("Média: ", media)

#Declarando a função relatorio que recebe **kwargs como parâmetro
def relatorio(**dados):

    #loop que verifica as chaves e valores passados pelos **dados
    for chave, valor in dados.items():
        #Imprime respectivamente a chave e o valor
        print(f"{chave}: {valor}")

#Declarando a função soma que recebe um número como parâmetro
def soma(numero):
    #O valor passado pelo parâmetro é somado a uma váriavel global
    soma = global_total + numero

    #Retorna a soma
    return print(soma)

#Declarando a função variavel local
def variavel_local():
    #Declarando váriavel local com o valor de uma string
    nome = "Bianca"

#Chamando função relatorio e passando informações com chave:valor por parametro
relatorio(nome='Bruna', idade=22, filha="Helena", marido="Jean")

#Chamando funçâo calcular média e passando alguns número por parâmetro
calcular_media(10, 5, 2, 6, 15)

#Chamando função soma, obtendo um número com o usuário que está sendo passado por parâmetro
soma(int(input("Digite um número: ")))

#Um erro irá ocorrer pois não é possível acessar uma váriavel local, fora da função
print(nome)