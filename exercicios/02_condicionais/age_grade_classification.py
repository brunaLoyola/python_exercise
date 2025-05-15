"""
Objetivo:
    Classificar a idade e nota de um usuário para determinar seu status.

Etapas:
    1. Perguntar a idade da pessoa e classificar como criança, adolescente ou adulto;
    2. Perguntar a nota do usuário e determinar seu status: aprovado, recuperação ou reprovado.
"""

#Obtém a idade do usuário
idade = int(input("Digite sua idade:"))

#Utiliza de condicionais para verificar as informações
if idade >= 0 and idade <=12:  #idade de 0 a 12 anos
    print("Você é uma criança")
elif idade >= 13 and idade <=17: #idade de 13 a 17 anos
    print("Você é um adolescente")
elif idade >= 18: #idade maior de 18 anos
    print("Você é um adulto")
else: 
    print("Idade inexistente") #Se não estiver dentro das condições anteriores

#Obtém a nota com o usuário e converte em float
nota = float(input("Digite sua de 0 a 10:"))

#Utiliza de condicionais para dizer a categoria do usuário
if nota >= 7: #nota maior ou igual a 7   
    print("Você está aprovado")
elif nota >= 5 and nota <=6.9: #nota maior ou igual a 5 e nota menor ou igual a 6.9
    print("Você está de recuperação")
elif nota >= 0 and nota < 5: #nota maior ou igual a 0 e nota menor que 5
    print("Você está reprovado")
else: #Se não estiver dentro das condições anteriores
    print("Nota inexistente")