# 65) Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos (incluindo os valores lidos na soma). Considere que o segundo valor lido será sempre maior que o primeiro valor lido.

soma = 0

while True:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    
    if valor2 > valor1:
        break
    else:
        print('O Segundo valor deve ser maior que o primeiro!')
    
for i in range(valor1, valor2 + 1):
    soma += i
            
print(f'Soma dos numeros inteiros entre {valor1} e {valor2}: {soma}')
