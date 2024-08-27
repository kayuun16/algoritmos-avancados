# 20) Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
print("Digite um valor")
valor_1 = float(input())

print("Digite outro valor")
valor_2 = float(input())

if valor_1 > valor_2:
    print(valor_1, valor_2)
else:
    print(valor_2, valor_1)
