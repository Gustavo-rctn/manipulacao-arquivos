def ler_arquivo(mensagem):
    with open(mensagem, 'r', encoding='utf-8') as mensagem_arquivo:
        dentro = mensagem_arquivo.read()
        print(dentro)

ler_arquivo('sla.txt')