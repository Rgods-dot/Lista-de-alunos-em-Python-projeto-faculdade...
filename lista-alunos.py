# SISTEMA DE CADASTRO DE ALUNOS

alunos = []


# Função para adicionar um aluno
def adicionar_aluno():
    print('\n--- ADICIONAR ALUNO ---')
    print('Digite (sair) para encerrar o cadastro de alunos.')

    while True:
        nome = input('\nDigite o nome do aluno: ')

        if nome.lower() == 'sair':
            print('Cadastro encerrado.')
            break

        while True:
            try:
                idade = int(input('Digite a idade do aluno: '))

                if idade > 0:
                    break
                else:
                    print('A idade deve ser maior que 0.')

            except ValueError:
                print('Digite uma idade válida.')

        while True:
            try:
                nota = float(input('Digite a nota do aluno (0 a 10): '))

                if 0 <= nota <= 10:
                    break
                else:
                    print('A nota deve estar entre 0 e 10.')

            except ValueError:
                print('Digite uma nota válida.')

        informações = {
            'nome': nome,
            'idade': idade,
            'nota': nota
        }

        alunos.append(informações)

        print('Aluno cadastrado com sucesso!')


    informações = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }

    alunos.append(informações)

    print('Aluno cadastrado!')


# Função para listar todos os alunos
def listar_alunos():
    print('\n--- LISTA DE ALUNOS ---')

    if len(alunos) == 0:
        print('Não há alunos cadastrados.')
        return

    for aluno in alunos:
        print(f'Nome: {aluno['nome']}')
        print(f'Idade: {aluno['idade']}')
        print(f'Nota: {aluno['nota']}')
        print('----------------------')


# Função para buscar um aluno pelo nome
def buscar_aluno():
    print('\n--- BUSCAR ALUNO ---')

    if len(alunos) == 0:
        print('Não há alunos cadastrados.')
        return

    nome_buscar = input('Digite o nome do aluno que deseja buscar: ')

    aluno_encontrado = False

    for aluno in alunos:
        if aluno['nome'].lower() == nome_buscar.lower():
            print('\nAluno encontrado!')
            print(f'Nome: {aluno['nome']}')
            print(f'Idade: {aluno['idade']}')
            print(f'Nota: {aluno['nota']}')

            aluno_encontrado = True
            break

    if not aluno_encontrado:
        print('Aluno não encontrado.')


# Função para remover um aluno
def remover_aluno():
    print('\n--- REMOVER ALUNO ---')

    if len(alunos) == 0:
        print('Não há alunos cadastrados.')
        return

    nome_remover = input('Digite o nome do aluno que deseja remover: ')

    aluno_encontrado = False

    for aluno in alunos:
        if aluno['nome'].lower() == nome_remover.lower():

            alunos.remove(aluno)

            aluno_encontrado = True

            print(f'Aluno ({nome_remover}) removido com sucesso.')

            break

    if not aluno_encontrado:
        print('Aluno não encontrado.')


# Função para calcular a média geral
def mostrar_media():
    print('\n--- MÉDIA GERAL ---')

    if len(alunos) == 0:
        print('Não há alunos cadastrados para calcular a média.')
        return

    soma = 0

    for aluno in alunos:
        soma = soma + aluno['nota']

    media = soma / len(alunos)

    print(f'Média geral das notas: {media:.2f}')


# MENU PRINCIPAL

while True:

    print('\n==============================')
    print('   SISTEMA DE CADASTRO')
    print('==============================')
    print('1. Adicionar aluno')
    print('2. Listar todos os alunos')
    print('3. Buscar aluno pelo nome')
    print('4. Remover aluno')
    print('5. Mostrar média geral das notas')
    print('6. Sair')
    print('==============================')

    opcao = input('Digite uma opção (1-6): ')

    if opcao == '1':
        adicionar_aluno()

    elif opcao == '2':
        listar_alunos()

    elif opcao == '3':
        buscar_aluno()

    elif opcao == '4':
        remover_aluno()

    elif opcao == '5':
        mostrar_media()

    elif opcao == '6':
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida. Digite uma opção de 1 a 6.')