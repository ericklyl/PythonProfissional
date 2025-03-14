try:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero:'))

    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    divs = n1/n2
    
    expo = n1**n2
    print(f'soma: {soma}')
    print(f'mult: {mult}')
    print(f'divs: {divs}')
    print(f'expo: {expo}')
except ZeroDivisionError:
    print('Não é possivel divisão por zero')

except ValueError:
    print('é preciso digitar um numero valido')
