lista = []

print('1. ADICIONAR ITEM')
print('2. REMOVER ITEM')
print('3. LISTAR COMPRA')
print('4. SAIR')
op = input('Quer fazer operação? [S/N] ').strip().upper()
while (op == 'S'):
    menu = int(input('Escolha uma opção: '))

    if (menu == 1):
        item = input('Qual o item a ser adicionado?')
        lista.append(item)
        print('Item adicionado!')
        print(f'A lista é {lista}')

    elif (menu ==2):
        item = input('Qual o item a ser excluido?')
        lista.remove(item)
        print('item excluido')
        print(f'A lista é {lista}')

    if (menu == 3):
        print(f'A lista é {lista}')

    if (menu == 4):
        print('fim')
        break
    op = input('Quer fazer operação?[S/N] ')

