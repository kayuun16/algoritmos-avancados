# 27) Ler um valor e escrever se é positivo, negativo ou zero.

print("Digite um valor:")
valor = float(input())

if valor > 0:
    print("Positivo!")
elif valor == 0:
    print("Zero!")
else:
    print("Negativo!")