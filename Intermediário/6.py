import time

def tempo_execucao(func):
    def wrapper(*args, **kwargs): #aceita qualquer argumento
        inicio = time.time() #vai marcar o tempo antes da execucao
        resultado = func(*args, **kwargs) #executa a função
        fim = time.time() #tempo após execução
        tempo_total = fim - inicio
        print(f'Tempo de execução: {tempo_total:.4f} segundos')
        return resultado
    return wrapper



@tempo_execucao
def soma(n):
    return sum(range(n))

print(soma(1000000))