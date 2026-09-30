def contar_linhas(nome_arquivo):
    total = 0
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            total += 1
    print(f'O arquivo possui {total} linhas.')

contar_linhas('alunos.txt')