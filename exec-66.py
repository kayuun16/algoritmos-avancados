# 66) O mesmo exercício anterior, mas agora, considere que o segundo valor lido poderá ser maior ou menor que o primeiro valor lido, ou seja, deve-se testá-los.

soma = 0

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))

for i in range(valor1, valor2 + 1):
    soma += i

print(f'Soma dos numeros inteiros entre {valor1} e {valor2}: {soma}')