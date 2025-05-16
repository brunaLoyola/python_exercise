"""Criar um programa interativo que:
Solicita dois números ao usuário;
Realiza:
Soma, subtração, multiplicação, divisão inteira e resto;
Compara os dois números:
Informa qual é maior, menor ou se são iguais;
Ao final, exibe um resumo organizado das operações e comparações feitas.
"""

numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))

soma = numero01 + numero02
subtracao = numero01 - numero02
multiplicacao = numero01 * numero02
divisao = numero01 / numero02

print("Resultado das operações e comparações dos números informados")
print(f" Soma: {soma} \n Subtração: {subtracao} \n Multiplicação: {multiplicacao} \n Divisão: {divisao}")

if numero01 == numero02:
    print("Os números são iguais")
elif numero01 > numero02:
    print(f"O primeiro número {numero01} é maior que o segundo número {numero02}")
else:
    print(f"O primeiro número {numero01} é menor que o segundo número {numero02}")