# 88) Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).

vet = [None] * 5

for i in range(5):
    vet[i] = float(input(f'Digite o valor na posicao {i + 1} do vetor: '))
    
novo_valor = float(input('Digite um valor: '))

if novo_valor in vet:
    vetor_sem_valor = []
    for valor in vet:
        if valor != novo_valor:
            vetor_sem_valor.append(valor)
    print('Novo vetor sem o valor digitado:')
    print(vetor_sem_valor)
else:
    print('O numero digitado nao se encontra no vetor')