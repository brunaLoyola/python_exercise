"""
Objetivo:
    Trabalhar com strings e validação de dados numéricos.

Etapas:
    1. Receber CPF com pontuação;
    2. Remover pontos e traços;
    3. Verificar se contém 11 dígitos numéricos.

Criado por: Bruna Loyola  
Data: 04/05/2025
"""

#Obtém o cpf do usuário, utilizando o .replace(), ele retira os .(pontos) e -(traços)
cpf = input("Digite seu cpf (com traços e pontos): ").replace(".", "").replace("-", "")

#Utiliza de condições para verificar se o cpf informado contém os 11 digitos 
if cpf.isdigit() and len(cpf)== 11: #.isdigit() significa que só deve existir númeral e o len() verifica o tamanho
    print(f"Seu cpf é {cpf} e contém os 11 dígitos")
else:
    print("Cpf incorreto, não contém os 11 dígitos numéricos")
