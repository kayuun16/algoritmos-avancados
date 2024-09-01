# 79) Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

total_alunos = 20
notas = [None] * total_alunos
soma_notas = 0
alunos_acima_media = 0

for i in range(total_alunos):
    notas[i] = float(input(f'Digite a nota do aluno {i + 1}: '))
    soma_notas += notas[i]
    
media = soma_notas / total_alunos

for nota in notas:
    if nota > media:
        alunos_acima_media += 1
        
print(f'A média da turma é: {media:.2f}')
print(f'Alunos com nota acima da média: {alunos_acima_media}')
