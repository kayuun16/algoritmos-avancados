# 33) Ler dois valores e imprimir uma das três mensagens a seguir:
#‘Números iguais’, caso os números sejam iguais
#‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
#‘Segundo maior’, caso o segundo seja maior que o primeiro.

print("Digite o primeiro valor:")
valor1 = float(input())

print("Digite o segundo valor:")
valor2 = float(input())

if valor1 > valor2:
    print("Primeiro e maior!")
elif valor1 == valor2:
    print("Numeros iguais")
else:
    print("Segundo maior!")