# 83) Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

valores = [None] * 20

for i in range(20):
    valores[i] = float(input(f'Digite o valor {i + 1}: '))
    
print('Valores na ordem inversa:')
for i in range(19, -1, -1):
    print(valores[i])