def contar_caracteres(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    print(f'Quantidade de caracteres: {len(conteudo)}')

contar_caracteres('texto.txt')