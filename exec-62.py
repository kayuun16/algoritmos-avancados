# 62) Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e escrever a média aritmética dessas notas lidas.

soma = 0
cont = 1

total_alunos = int(input('Ha quantos alunos na turma? '))

while cont <= total_alunos:
    notas = float(input(f'Qual a nota do aluno {cont}? '))
    soma += notas
    cont += 1
    
media = soma / total_alunos

print(f'Media da turma: {media:.2f}')
