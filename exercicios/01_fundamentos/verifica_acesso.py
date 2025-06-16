#Crie um programa que verifica a idade e se possui autorização de um usuário para determinar o acesso.

idade = int(input('Digite sua idade (número inteiro): '))
autorizacao = input('Tem autorização (S ou N): ').upper()

if idade >= 18 or autorizacao == 'S':
    print('Pode entrar!')
elif idade < 18 or idade > 0 or autorizacao == 'N': 
    print('Acesso negado')
else:
    print('Opção inválida')