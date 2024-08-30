# 53) Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO

N0 = int(input("Digite um valor maior que 0:"))

N = N0 + 1

for valores in range(1, N):
    print(valores)