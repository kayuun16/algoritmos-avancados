# 78) Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armaze os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

nomes = [None] * 4

for i in range(4):
    nomes[i] = str(input(f'Digite o nome da pessoa {i + 1}: '))
    
nome_busca = str(input('Digite o nome que deseja buscar: '))

if nome_busca in nomes:
    print('ACHEI')
else:
    print('NAO ACHEI')