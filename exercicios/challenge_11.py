def listar_aprovados(nome_arquivo):
    print('Alunos aprovados:')
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(';')
            if float(nota) >= 6.0:
                print(f'{nome} - {nota}')

listar_aprovados('alunos.txt')