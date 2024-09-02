# 91) Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

vet = [None] * 10

for i in range(10):
    vet[i] = float(input(f'Digite um valor na posicao {i + 1} do vetor: '))

encontrou_repetidos = False

for i in range(10):
    valor = vet[i]
    
    for j in range(i):
        if vet[j] == valor:
            if not encontrou_repetidos:
                print('Existem valores repetidos no vetor.')
                encontrou_repetidos = True
            print(f'O valor {valor} se repetiu na posicao {i}.')
            break
        
if not encontrou_repetidos:
    print('Nao existem valores repetidos no vetor.')