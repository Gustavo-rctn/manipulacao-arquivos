def calcular_estoque(nome_arquivo):
    produtos = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(';')
            produtos.append({
                'nome': nome,
                'preco': float(preco),
                'quantidade': int(quantidade)
            })

    valor_total = 0.0
    for p in produtos:
        valor_total += p['preco'] * p['quantidade']

    print(f'Valor total do estoque: R$ {valor_total:.2f}')

calcular_estoque('produtos.txt')