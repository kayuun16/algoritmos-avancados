# 84) Faça um algoritmo para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.
    
tamanho_vetor = int(input('Qual o tamanho do vetor? '))

A = [None] * tamanho_vetor
B = [None] * tamanho_vetor
Soma = [None] * tamanho_vetor

for i in range(tamanho_vetor):
    A[i] = float(input(f'Digite o valor na posicao {i + 1} do vetor A: '))
    
for i in range(tamanho_vetor):
    B[i] = float(input(f'Digite o valor na posicao {i + 1} do vetor B: '))
    
for i in range(tamanho_vetor):
    Soma[i] = A[i] + B[i]
    
print('Vetor Soma:')
for i in range(tamanho_vetor):
    print(f'{Soma[i]}')