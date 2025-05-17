from funcoes import cadastrar, listar_alunos, media_notas

opcao = 1

while opcao != 4:
    opcao = int(input("Seja Bem-vindo(a):\n 01 - Cadastrar aluno \n 02 - Ver lista de alunos \n 03 - Média das notas \n 04 - Sair\n"))

    if opcao <= 0 or opcao >= 5:
        print("Opção incorreta, tente novamente !")
        continue
    elif opcao == 1:
        nome_aluno = input("Digite seu nome: ")
        idade_aluno = int(input("Digite sua idade: "))
        nota_aluno = float(input("Digite sua nota: "))
        dados_aluno = {
            "nome": nome_aluno,
            "idade": idade_aluno,
            "nota": nota_aluno
        }
        cadastrar(dados_aluno)
        continue
    elif opcao == 2:
        listar_alunos()
        continue
    elif opcao == 3:
        media_notas()
        continue