# 41) Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula abaixo e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:

# Média_de_aproveitamento = (N1 + (N2 * 2) + (N3 * 3)) / 7 

# A atribuição de conceitos obedece a tabela abaixo:

# A > = 9,0
# B > = 7,5 e < 9,0
# C > = 6,0 e < 7,5
# D < 6,0

print("Qual a sua nota na primeira avaliacao?")
nota1 = float(input())

print("Qual a sua nota na segunda avaliacao?")
nota2 = float(input())

print("Qual a sua nota na terceira avaliacao?")
nota3 = float(input())

media_aproveitamento = (nota1 + (nota2 * 2) + (nota3 * 3)) / 7

if media_aproveitamento >= 9:
    conceito = "A"
    print(f"Media de aproveitamento: {media_aproveitamento:.2f}")
    print(f"Conceito: {conceito}")
elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
    conceito = "B"
    print(f"Media de aproveitamento: {media_aproveitamento:.2f}")
    print(f"Conceito: {conceito}")
elif media_aproveitamento >= 6 and media_aproveitamento < 7.5:
    conceito = "C"
    print(f"Media de aproveitamento: {media_aproveitamento:.2f}")
    print(f"Conceito: {conceito}")
else:
    conceito = "D"
    print(f"Media de aproveitamento: {media_aproveitamento:.2f}")
    print(f"Conceito: {conceito}")