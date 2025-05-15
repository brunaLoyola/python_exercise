"""
Objetivo:
    Coletar números do usuário, filtrar os pares e exibir estatísticas.

Etapas:
    1. Solicitar 10 números e armazenar em uma lista;
    2. Criar nova lista com apenas os pares;
    3. Exibir a lista completa, os pares e a soma dos pares.
"""

#Declara duas listas vazias que serão tratadas 
lista_numeros = [] #Números que o usuário digitar
lista_par = [] #Números pares da 'lista_numeros'

#Atráves de um loop, o usuário terá que digitar 10 números
for numero in range(1, 11):
    num = int(input(f"Digite o {numero}° número: "))
    lista_numeros.append(num) #O número digitado está sendo inserido na 'lista_numeros'
    
#Atráves de um loop ele passa por todos os indíces da 'lista_numeros'
for numero in lista_numeros:
    if numero % 2 == 0: #Com uma condição ele verifica se é um número par
        lista_par.append(numero) #E adiciona o número par a 'lista_par'

#Imprimindo a lista completa
print("Lista completa: ",lista_numeros) 

#Imprimindo a lista dos pares
print("Lista de números pares: ",lista_par)

#Somando os itens da lista dos números pares
print("Soma dos números par: ", sum(lista_par))