def classificar_alunos(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(';')
            nota_float = float(nota)

            if nota_float >= 6.0:
                status = 'Aprovado'
            elif nota_float >= 4.0:
                status = 'Recuperação'
            else:
                status = 'Reprovado'

            print(f'{nome} - {nota} - {status}')

classificar_alunos('alunos.txt')