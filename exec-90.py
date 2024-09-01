# 90) Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

vet = [None] * 30
cont_valor_random = 0

for i in range(30):
    vet[i] = float(input(f'Digite um valor na posicao {i + 1} do vetor: '))
    
valor_random = float(input('Digite um valor qualquer: '))

for valor in vet:
    if valor == valor_random:
        cont_valor_random += 1

print(f'O valor {valor_random} aparece {cont_valor_random} vez(ez) no vetor.')