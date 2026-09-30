def carregar_alunos():
    alunos = []
    try:
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(';')
                if len(partes) == 4:
                    alunos.append({
                        'id': int(partes[0]),
                        'nome': partes[1],
                        'idade': int(partes[2]),
                        'curso': partes[3]
                    })
    except FileNotFoundError:
        pass
    return alunos

def salvar_alunos(alunos):
    with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
        for a in alunos:
            arquivo.write(f"{a['id']};{a['nome']};{a['idade']};{a['curso']}\n")

def sistema_alunos():
    alunos = carregar_alunos()

    while True:
        print('\n===== SISTEMA DE ALUNOS =====')
        print('1 - Listar alunos\n2 - Buscar aluno\n3 - Cadastrar aluno\n4 - Remover aluno\n5 - Alterar aluno\n6 - Sair')
        opcao = input('Escolha: ')

        if opcao == '1':
            for a in alunos:
                print(f"{a['id']} - {a['nome']} - {a['idade']} anos")

        elif opcao == '2':
            id_busca = int(input('Digite o ID: '))
            aluno = next((a for a in alunos if a['id'] == id_busca), None)
            if aluno:
                print(f"\nAluno encontrado:\n{aluno['nome']}\n{aluno['idade']} anos\n{aluno['curso']}")
            else:
                print('\nAluno não encontrado!')

        elif opcao == '3':
            novo_id = max([a['id'] for a in alunos], default=0) + 1
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            curso = input('Curso: ')
            alunos.append({'id': novo_id, 'nome': nome, 'idade': idade, 'curso': curso})
            salvar_alunos(alunos)
            print('Aluno cadastrado com sucesso!')

        elif opcao == '4':
            id_rem = int(input('ID do aluno a remover: '))
            alunos = [a for a in alunos if a['id'] != id_rem]
            salvar_alunos(alunos)
            print('Remoção concluída!')

        elif opcao == '5':
            id_alt = int(input('ID do aluno a alterar: '))
            encontrado = False
            for a in alunos:
                if a['id'] == id_alt:
                    a['nome'] = input('Novo nome: ')
                    a['idade'] = int(input('Nova idade: '))
                    a['curso'] = input('Novo curso: ')
                    encontrado = True
                    break
            if encontrado:
                salvar_alunos(alunos)
                print('Alteração efetuada!')
            else:
                print('Aluno não encontrado!')

        elif opcao == '6':
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida!')

sistema_alunos()