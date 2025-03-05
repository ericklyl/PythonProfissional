contatos = {}

print('1. ADICIONAR CONTATO')
print('2. REMOVER CONTATO')
print('3. BUSCAR CONTATO')
print('4. SAIR')

op = input('Quer fazer operação? [S/N] ').strip().upper()
while (op == 'S'):
    menu = int(input('Escolha uma opção: '))

    if (menu == 1):
        nome = input('Qual o CONTATO a ser adicionado? ')
        idade = int(input('Qual a idade do contato? '))
        telefone = int(input('Qual o telefone a ser adicionado? '))
        contatos[nome] = {'idade': idade, "telefone": telefone}

        
        print('contato adicionado!')
        print(f'A lista é {contatos}')

    elif (menu ==2):
        nome = input('Qual o contato a ser excluido? ')
        del contatos[nome]
        print('contato excluido')
        print(f'A lista é {contatos}')

    if (menu == 3):
        nome = input('Qual o contato a ser buscado? ')
        print(f'A lista é {contatos[nome]}')

    if (menu == 4):
        print('fim')
        break