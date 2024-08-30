# 63) Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.

soma = 0
cont = 1

while cont <= 10:
    valores = float(input('Digite um valor: '))
    soma += valores
    cont += 1
    
print(f'Soma dos valores: {soma}')
