# 87) O mesmo exercício anterior, mas depois de ordenar os elementos do vetor em ordem crescente, deve ser lido mais um número qualquer e inserir esse novo número na posição correta, ou seja, mantendo a ordem crescente do vetor.

vet = [None] * 10

for i in range(10):
    vet[i] = float(input('Digite um valor: '))
    
vet.sort()

novo_valor = float(input('Digite um novo valor: '))

inserido = False
for i in range(10):
    if novo_valor <= vet[i]:
        vet.insert(i, novo_valor)
        inserido = True
        break

if not inserido:
    vet.append(novo_valor)

print('Vetor em ordem crescente:')
print(vet)