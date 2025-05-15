"""
Objetivo:
    Realizar cálculos com base na operação escolhida pelo usuário.

Etapas:
    1. Solicitar dois números do usuário;
    2. Perguntar qual operação deseja realizar (+, -, *, /);
    3. Exibir o resultado da operação selecionada.
"""

#Obtém dois números
numero_01 = int(input("Digite o primeiro número:"))
numero_02 = int(input("Digite o segundo número:"))

#Obtém  a operação (+, -, *, /)
operacao = input("Digite a operação (+, -, *, /):")

#Utiliza de condições para fzaer o calculo de acordo com a escolha do usuário
if operacao in '+':
    print(f"Resultado: {numero_01 + numero_02}")
elif operacao in '-':
    print(f"Resultado: {numero_01 - numero_02}")
elif operacao in '*':
    print(f"Resultado: {numero_01 * numero_02}")
elif operacao in '/':
    print(f"Resultado: {numero_01 / numero_02}")
#Caso o usuário tenha digitado uma operação inválida.
else:
    print("Operação inválida!")
