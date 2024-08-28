# 31) Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.

print("Digite o valor do lado A")
A = float(input())

print("Digite o valor do lado B")
B = float(input())

print("Digite o valor do lado C")
C = float(input())

if A < B + C and B < C + A and C < A + B:
    print("Formam um triangulo!")
else:
    print("Nao formam um triangulo!")