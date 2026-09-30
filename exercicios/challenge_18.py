def gerenciar_notas(nome_arquivo):
    alunos = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(';')
            nome = partes[0]
            notas = [float(n) for n in partes[1:]]
            alunos.append({'nome': nome, 'notas': notas})

    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        status = 'Aprovado' if media >= 6.0 else 'Reprovado'
        print(f"{aluno['nome']} - Média: {media:.2f} - {status}")

gerenciar_notas('notas.txt')