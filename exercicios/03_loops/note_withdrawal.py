"""
Objetivo:
    Calcular as notas de saque que um valor pode ser retirado.

Etapas:
    1. Solicitar um valor inteiro para saque;
    2. Determinar quantas notas de 100, 50, 20, 10, 5 e 1 podem ser entregues.
"""

#Obtém o valor a ser sacado
valor = int(input("Digite o valor inteiro que será retirado: "))
notas = [100, 50, 20, 10, 5, 1] #Cria uma lista com as possíveis notas a ser usada

#Diga com quantas notas de 100, 50, 20, 10, 5 e 1 esse valor pode ser sacado
print("Notas que serão entregues: ")

#Percorre a listas de notas
for nota in notas:
    quantidade = valor // nota #Divide o valor total pelo valor da nota
    valor %= nota   #Atualiza o valor restante após retirar essas notas

    #Condição de enquanto o valor for maior que 0, irá imprimir a quantidade de notas 
    if quantidade > 0: 
        print(f"{quantidade} nota(s) de R${nota}")