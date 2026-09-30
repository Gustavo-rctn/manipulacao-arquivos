def gerenciar_tarefas():
    tarefas = []

    try:
        with open('tarefas.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                tarefas.append(linha.strip())
    except FileNotFoundError:
        pass

    opcao = ''
    while opcao != '4':
        print('\n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Remover tarefa\n4 - Sair')
        opcao = input('Escolha: ')

        if opcao == '1':
            nova = input('Digite a tarefa: ')
            tarefas.append(nova)
            with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
                for item in tarefas:
                    arquivo.write(f'{item}\n')
        elif opcao == '2':
            for i, t in enumerate(tarefas, 1):
                print(f'{i} - {t}')
        elif opcao == '3':
            idx = int(input('Número da tarefa para remover: ')) - 1
            if 0 <= idx < len(tarefas):
                tarefas.pop(idx)
                with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
                    for item in tarefas:
                        arquivo.write(f'{item}\n')
            else:
                print('Tarefa inválida!')
        elif opcao == '4':
            print('Saindo...')
        else:
            print('Opção inválida!')

gerenciar_tarefas()