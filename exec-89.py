# 89) Faça um algoritmo para ler dois vetores V1 e V2 de 15 números cada. Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.

V1 = [None] * 15
V2 = [None] * 15

valores_repetidos = 0

for i in range(15):
    V1[i] = float(input(f'Digite um valor na posicao {i + 1} do vetor V1: '))

for i in range(15):
    V2[i] = float(input(f'Digite um valor na posicao {i + 1} do vetor V2: '))

for i in range(15):
    if V1[i] == V2[i]:
        valores_repetidos += 1

print(f'Quantidade de vezes que V1 e V2 possuem os mesmos valores nas mesmas posições: {valores_repetidos}')