# 62) Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e escrever a média aritmética dessas notas lidas.

soma = 0
total_alunos = int(input('Ha quantos alunos na turma? '))

for alunos in range (1, total_alunos + 1):
    notas = float(input(f'Qual a nota do aluno {alunos}? '))
    soma += notas
    
media = soma / total_alunos

print(f'Media da turma: {media:.1f}')