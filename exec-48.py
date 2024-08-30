# 48) Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota.

while True:
    print("Qual a nota na primeira avaliacao?")
    nota1 = float(input())

    print("Qual a nota na segunda avaliacao?")
    nota2 = float(input())
    
    if nota1 <= 10 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f"Media: {media:.1f}")
        break
    else:
        if nota1 > 10 or nota2 > 10:
            print("Nota invalida!")