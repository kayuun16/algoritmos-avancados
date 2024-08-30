# 54) Modifique o exercício anterior para aceitar somente valores maiores que 0 para N. Caso o valor informado (para N) não seja maior que 0, deverá ser lido um novo valor para N.

N = 0

while N <= 0:
    N = int(input("Digite um valor maior que 0:"))
    
for valores in range (1, N + 1):
    print(valores)