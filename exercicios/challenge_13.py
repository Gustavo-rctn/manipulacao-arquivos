def menu_arquivo():
    opcao = ''
    while opcao != '4':
        print('\n1 - Ler arquivo\n2 - Adicionar texto\n3 - Sobrescrever arquivo\n4 - Sair')
        opcao = input('Escolha: ')

        if opcao == '1':
            try:
                with open('notas.txt', 'r', encoding='utf-8') as arquivo:
                    print(arquivo.read())
            except FileNotFoundError:
                print('Arquivo ainda não existe!')
        elif opcao == '2':
            texto = input('Digite o texto: ')
            with open('notas.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{texto}\n')
        elif opcao == '3':
            texto = input('Digite o novo texto: ')
            with open('notas.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write(f'{texto}\n')
        elif opcao == '4':
            print('Programa encerrado.')
        else:
            print('Opção inválida!')

menu_arquivo()