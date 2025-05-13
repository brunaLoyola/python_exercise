"""
Objetivo:
    Calcular a média de quatro notas e determinar o status do aluno.

Etapas:
    1. Solicitar quatro notas ao aluno;
    2. Calcular a média e exibir se o aluno foi aprovado, de recuperação ou reprovado;
    3. Exibir também a maior e menor nota.

Criado por: Bruna Loyola
Data: 30/04/2025
"""

lista_numeros = []
for numero in range(1, 5):
    lista_numeros.append(int(input(f"Digite sua {numero}° nota:"))) 

#Calcule a média
media = sum(lista_numeros) / 4

#Se for ≥ 7, diga que foi aprovado
if media >=7 and media <= 10:
    print("Você foi aprovado!")
# Entre 5 e 6.9, recuperação.
elif media <= 7 and media >= 5:
    print("Você está de recuperação")
elif media > 10 or media < 0:
    print("Nota informada inválida")
#Abaixo de 5, reprovado
else:
    print("Reprovado!")
#Mostre também a maior e menor nota.
print(f" A sua maior nota é: {max(lista_numeros)} \n A sua menor nota é: {min(lista_numeros)}")