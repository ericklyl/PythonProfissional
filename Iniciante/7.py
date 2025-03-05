def fatorial(n):
    r = 1
    for i in range(n,1,-1):
        r = r * i
    return r

n = int(input('Qual o numero? '))
print(fatorial(n))