# 82) Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.

A = [None] * 10

for i in range(10):
    A[i] = float(input(f'Digite um valor na posicao {i + 1} do vetor A: '))
    
X = float(input('Digite um valor: '))

M = [None] * 10

for i in range(10):
    M[i] = A[i] * X
    
print('Vetor M:')
for i in range(10):
    print(f'{M[i]}')
