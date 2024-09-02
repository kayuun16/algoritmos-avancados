# 70) Faça um programa que leia 100 valores e no final, escreva o maior e o menor valor lido.

maior_valor = 0
menor_valor = 0

for i in range(100):
    valor = float(input('Digite um valor: '))
    print(valor)
    
    if maior_valor == 0 or valor > maior_valor:
        maior_valor = valor
    elif menor_valor == 0 or valor < menor_valor:
        menor_valor = valor
        
print(f'Maior valor: {maior_valor} / Menor valor: {menor_valor}')
