"""
Objetivo:
    Solicitar números ao usuário e somá-los até que ele digite zero.

Etapas:
    1. Solicitar números em um loop;
    2. Somar os valores digitados;
    3. Encerrar quando o número zero for digitado;
    4. Exibir a soma total.
"""

#Declara duas variaveis inteiras que serão tratadas
soma = 0
numero_usuario = 1 #Inicia em 1 para poder entrar no while

#Enquanto o número for diferente de 0, o while continuará funcionando
while numero_usuario != 0:
    numero_usuario = int(input("Digite um número inteiro a ser somado (digite 0 para sair): "))
    soma += numero_usuario 

#Imprime o total da soma dos números digitados pelo usuário
print("Total: ", soma)