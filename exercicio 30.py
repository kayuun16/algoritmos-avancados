# 30) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

print("Digite um valor:")
valor_1 = float(input())

print("Digite outro valor:")
valor_2 = float(input())

print("Digite mais um valor:")
valor_3 = float(input())

if valor_1 < valor_2 and valor_1 < valor_3:
    if valor_2 < valor_3:
        print(valor_1, valor_2, valor_3)
    else:
        print(valor_1, valor_3, valor_2)
elif valor_2 < valor_1 and valor_2 < valor_3:
    if valor_1 < valor_3:
        print(valor_2, valor_1, valor_3)
    else:
        print(valor_2, valor_3, valor_1)
else:
    if valor_1 < valor_2:
        print(valor_3, valor_1, valor_2)
    else:
        print(valor_3, valor_2, valor_1)