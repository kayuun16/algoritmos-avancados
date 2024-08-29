# 29) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

print("Digite um valor:")
valor_1 = float(input())

print("Digite outro valor:")
valor_2 = float(input())

print("Digite mais um valor:")
valor_3 = float(input())

if valor_1 < valor_2 and valor_1 < valor_3:
    soma = valor_2 + valor_3
elif valor_2 < valor_1 and valor_2 < valor_3:
    soma = valor_1 + valor_3
else:
    soma = valor_1 + valor_2
    
print("Soma dos maiores valores: " + str(soma))
