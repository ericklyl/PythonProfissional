texto = input('Digite um texto: ').upper().strip()
vogais = 0
con = 0
for i in texto:
    if i in ('A', 'E', 'I', 'O','U'):
        vogais += 1
    else:
        con += 1

print('Vogais: ', vogais)
print('Consoantes: ', con)