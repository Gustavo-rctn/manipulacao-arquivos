def cadastrar_produtos(nome_arquivo):
    produtos = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(';')
            obj = {
                'nome': nome,
                'preco': float(preco),
                'quantidade': int(quantidade)
            }
            produtos.append(obj)

    print(produtos)

cadastrar_produtos('produtos.txt')