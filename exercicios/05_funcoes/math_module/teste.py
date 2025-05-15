"""
Objetivo:
    Criar módulo de operações matemáticas e testar importações.

Etapas:
    1. Criar arquivo matematica.py com funções: soma, subtrai, multiplica, divide;
    2. Criar arquivo teste.py e importar funções usando diferentes formas;
    3. Testar execução das funções importadas.

Criado por: Bruna Loyola  
Data: 02/05/2025
"""
#Importando o módulo com as funções de diferentes formas 
import matematica #importando o módulo todo
from matematica import subtrai, divide #importando apenas as funções subtrais e divide
from matematica import multiplica as multiplicacao #importando a função multiplica e modificando seu nome para multiplicacao

#Obtendo dois números com o usuário
numero01_usuario = int(input("Digite o primeiro número: "))
numero02_usuario = int(input("Digite o segundo número: "))

#Imprimindo o retorno das funções enquanto elas são chamadas dentro do print e passando os números obtidos com o usuário por parametro
print(f"Resultado da soma: {matematica.soma(numero01_usuario, numero02_usuario)}")
print(f"Resultado da subtração: {subtrai(numero01_usuario, numero02_usuario)}")
print(f"Resultado da divisão: {divide(numero01_usuario, numero02_usuario)}")
print(f"Resultado da multiplicação: {multiplicacao(numero01_usuario, numero02_usuario)}")
