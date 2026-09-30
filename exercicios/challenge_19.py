def gerar_relatorio(nome_arquivo):
    vendas = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(';')
            vendas.append({
                'vendedor': vendedor,
                'produto': produto,
                'valor': float(valor)
            })

    total = sum(v['valor'] for v in vendas)
    print(f'TOTAL DE VENDAS: R$ {total:.2f}\n')

    qtd_vendas = {}
    totais_vendedor = {}

    for v in vendas:
        vend = v['vendedor']
        qtd_vendas[vend] = qtd_vendas.get(vend, 0) + 1
        totais_vendedor[vend] = totais_vendedor.get(vend, 0.0) + v['valor']

    print('Quantidade de vendas:')
    for vend, qtd in qtd_vendas.items():
        print(f'{vend}: {qtd}')

    top = max(totais_vendedor, key=totais_vendedor.get)
    print(f'\nMaior valor em vendas: {top} (R$ {totais_vendedor[top]:.2f})')

gerar_relatorio('vendas.txt')