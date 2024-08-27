# 36) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha

print("Qual a idade do primeiro homem?")
idade_h1 = int(input())

print("Qual a idade do segundo homem?")
idade_h2 = int(input())

print("Qual a idade da primeira mulher?")
idade_m1 = int(input())

print("Qual a idade da segunda mulher?")
idade_m2 = int(input())

homem_velho = max(idade_h1, idade_h2)
homem_novo = min(idade_h1, idade_h2)

mulher_velha = max(idade_m1, idade_m2)
mulher_nova = min(idade_m1, idade_m2)

soma_idade = homem_velho + mulher_nova
produto_idade = homem_novo * mulher_velha
        
print("Soma das idades do mais velho com a mais nova: " + str(soma_idade))
print("Produto das idades do mais novo com a mais velha: " + str(produto_idade))