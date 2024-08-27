# 13) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:
# media_final = (n1 * 2 + n2 * 3 + n3 * 5) / 10

print("Digite sua primeira nota:")
nota_1 = float(input())

print("Digite sua segunda nota:")
nota_2 = float(input())

print("Digite sua terceira nota:")
nota_3 = float(input())

media_final = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5)) / 10

print("Media final: " + str(media_final))