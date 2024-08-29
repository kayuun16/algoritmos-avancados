# 45) Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura ENQUANTO).

print("Digite o primeiro valor:")
valor1 = float(input())

divisao = 0

while True:
    print("Digite o segundo valor: (diferente de zero!)")
    valor2 = float(input())
    if valor2 != 0:
        divisao = valor1 / valor2
        break
    else:
        print("O segundo valor nao pode ser igual a 0!")
    
print(f"Resultado da divisao de {valor1} por {valor2}: {divisao:.2f}")