# 64) Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.

soma = 0
cont = 1

while cont <= 10:
    valores = float(input('Digite um valor: '))
    if valores < 40:
        soma += valores
    cont += 1
        
print(f'Soma dos valores inferiores a 40: {soma}')