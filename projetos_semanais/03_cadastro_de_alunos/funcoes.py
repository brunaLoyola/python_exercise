alunos = []
def cadastrar(dados):
    alunos.append(dados)
    print("Aluno(a) cadastrado !!")

def listar_alunos():
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")


def media_notas():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum([aluno['nota'] for aluno in alunos]) / len(alunos)
    print(f"Média das notas: {media:.2f}")