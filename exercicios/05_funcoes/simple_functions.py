"""
Objetivo:
    Criar funções simples com estrutura condicional e retorno.

Etapas:
    1. Criar função apresentar() que imprime nome e idade;
    2. Criar função dobro(numero) que retorna o dobro;
    3. Criar função multiplica(a, b);
    4. Criar função eh_par(numero);
    5. Criar função boas_vindas(nome).

Criado por: Bruna Loyola  
Data: 02/05/2025
"""

#Declarando função apresentar
def apresentar():
    #Obtem as informações de nome e idade com o usuário
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    #Imprime uma mensagem personalizada
    print(f"Seu nome é {nome} e sua idade {idade} anos")

#Declarando função dobro
def dobro(numero): #Recebe atráves do parametro um número
    return print("O dobro do número é: ", numero*2) #retorna imprimindo na tela o numero multiplicado por 02

#Declarando função multiplica
def multiplica(a, b): #Recebe atráves do parametro um dois números
    print(f"{a} x {b} =", a*b) #Imprime a multiplicação dos números 

#Declarando função eh_par
def eh_par(numero): #Recebe atráves do parametro um número
    if numero % 2 == 0: #Atáves de uma condição verifica se é par ou não, utilizando o resto da divisão
        print("É par")
    else:
        print("Não é par")

#Declarando função voas_vindas
def boas_vindas(nome): #Recebe atráves do parametro um nome
    print(f"Seja bem vindo(a) {nome}") #Imprime uma mensagem personalizada com o nome recebido

#Chamando a função apresentar
apresentar()

#Obtendo um número com o usuário
numero_dobro = int(input("Digite o número: "))
#Chamando a função dobro e passando por parametro o número que o usuário informou
dobro(numero_dobro)

#Obtendo dois números com o usuário
multiplica_primeiro = int(input("Digite o primeiro número: "))
multiplica_segundo = int(input("Digite o segundo número: "))

#Chamando a função multiplica e passando por parametro os números que o usuário informou
multiplica(multiplica_primeiro, multiplica_segundo)

#Obtendo um número com o usuário
par = int(input("Digite um número: "))
#Chamando a função par e passando por parametro o número que o usuário informou
eh_par(par)

#Obtendo um nome com o usuário
nome = input("Digite seu nome: ")

#Chamando a função boas_vindas e passando por parametro o nome que o usuário informou
boas_vindas(nome)