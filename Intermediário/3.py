texto = input('Digite um texto: ')

#salvar texto
with open("texto.txt", "w", encoding="utf-8") as textinho:
    textinho.write(texto)

print('Texto salvo')

with open('texto.txt', 'r', encoding='utf-8') as textinho:
    c = textinho.read()

print(c)