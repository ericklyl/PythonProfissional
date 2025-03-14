def numeros_primos():
    num = 2
    while True:
        if eh_primo(num):
            yield num
        num += 1


def eh_primo(n):
    if n< 2:
        return False
    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            return False
    return True


gen = numeros_primos()

print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 5
print(next(gen))  # 7
print(next(gen))  # 11
print(next(gen))  # 13
