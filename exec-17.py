# 17) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
print("Digite sua nota da primeira avaliacao")
nota_1 = float(input())

print("Digite sua nota da segunda avaliacao")
nota_2 = float(input())

media = float(nota_1 + nota_2)/2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
    
print("Sua média : " + str(media))
