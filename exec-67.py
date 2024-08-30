#67) Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros entre 15 (inclusive) e 100 (inclusive).

inicio = 15
fim = 100
soma = 0
cont = 0

for i in range(inicio, fim + 1):
    soma += i
    cont += 1
    
media = soma / cont

print(f'Media aritmetica dos valores entre {inicio} e {fim}: {media:.2f}')