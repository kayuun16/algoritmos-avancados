# 80) Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.

Q = [None] * 20
for i in range(20):
    while True:
        valor = float(input(f'Digite um valor positivo na posicao {i + 1}: '))
        if valor >= 0:
            Q[i] = valor
            break
        else:
            print('Valor negativo! Tente novamente!')
             
maior_valor = 0
posicao_maior_valor = 0

for i in range(20):
    if Q[i] > maior_valor:
        maior_valor = Q[i]
        posicao_maior_valor = i
        
print(f'Maior valor: {maior_valor}')
print(f'Posicao do maior valor: {posicao_maior_valor + 1}')