n1 = int(input('Digite um numero: '))
ask = input('Quer contagem regressiva[S/N]? ')
while(ask == 'S'):
    for i in range(n1, 0,-1):
        print(i)
    n1 = int(input('Digite um numero: '))
    ask = input('Quer contagem regressiva[S/N]? ')
    


print('encerrando')
