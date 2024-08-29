# 30) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

print("Digite um valor:")
valor_1 = float(input())

print("Digite outro valor:")
valor_2 = float(input())

print("Digite mais um valor:")
valor_3 = float(input())

valores = [valor_1, valor_2, valor_3]

valores.sort()

print("Valores em ordem crescente: " + str(valores))
