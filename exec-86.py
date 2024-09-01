# 86) Faça um algoritmo para ler 10 números e armazenar em um vetor. Após isto, o algoritmo deve ordenar os números no vetor em ordem crescente. Escrever o vetor ordenado.

vet = [None] * 10

for i in range(10):
    vet[i] = float(input('Digite um valor: '))
    
vet.sort()

print('Vetor em ordem crescente:')
print(vet)