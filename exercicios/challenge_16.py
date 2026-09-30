def buscar_produto(nome_arquivo):
    produtos = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(';')
            produtos.append({
                'nome': nome,
                'preco': float(preco),
                'quantidade': int(quantidade)
            })

    busca = input('Digite o produto: ')
    encontrado = False

    for item in produtos:
        if item['nome'].lower() == busca.lower():
            print('\nProduto encontrado!')
            print(f"Nome: {item['nome']}")
            print(f"Preço: R$ {item['preco']:.2f}")
            print(f"Quantidade: {item['quantidade']}")
            encontrado = True
            break

    if not encontrado:
        print('\nProduto não encontrado!')

buscar_produto('produtos.txt')