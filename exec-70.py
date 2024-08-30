# 70) Faça um programa que leia 100 valores e no final, escreva o maior e o menor valor lido.

import random

maior_valor = 0
menor_valor = 0

for _ in range(100):
    valor = random.randint(-1000, 1000)
    print(valor)
    
    if maior_valor == 0 or valor > maior_valor:
        maior_valor = valor
    elif menor_valor == 0 or valor < menor_valor:
        menor_valor = valor
        
print(f'Maior valor: {maior_valor} / Menor valor: {menor_valor}')